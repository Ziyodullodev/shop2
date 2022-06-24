from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Mahsulot

from buyurtma.models import Savat, Tanlangan, Sotibol

from userapp.models import Client




class Page_profile_wishlist(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                m = Client.objects.get(user=request.user)
                t = Tanlangan.objects.filter(mijoz=m)
                return render(request, 'page-profile-wishlist.html', {"tanlangan": t})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Add_profile_wishlist(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                mijoz = Client.objects.get(user=request.user)
                savat = Savat.objects.get(id=pk)
                mahsulot = Mahsulot.objects.get(id=savat.mahsulot.id)
                tanlangan = Tanlangan.objects.filter(mijoz=mijoz)
                for i in tanlangan:
                    if i.mahsulot == mahsulot:
                        return redirect('page-shopping-cart')

                Tanlangan.objects.create(
                    mijoz=mijoz,
                    mahsulot=mahsulot,
                    son=savat.son
                )
                return redirect('page-shopping-cart')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"mahsulot": mahsulotlar})

        else:
            return redirect('/page-user-login')

class Page_profile_delete_wishlist(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            q = Tanlangan.objects.get(id=pk)
            q.delete()
            return redirect('page-profile-wishlist')
        else:
            return redirect('/page-user-login')


class Page_shopping_cart(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                mij = Client.objects.get(user=request.user)
                tanlangan = Tanlangan.objects.filter(mijoz=mij)
                savat = Savat.objects.filter(mijoz=mij)
                umumiy = 0
                for i in savat:
                    umumiy = umumiy + (i.son * i.mahsulot.narx)
                aksiya = 0
                for i in savat:
                    aksiya = aksiya + (i.son * ((i.mahsulot.aksiya * i.mahsulot.narx)/100))
                return render(request, 'page-shopping-cart.html', {"savat": savat, "umumiy": umumiy, "aksiya": aksiya, "allprice": umumiy-aksiya, "tanlangan": tanlangan})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Add_shopping_cart(View):
    def get(self, request, pk):
        m = Client.objects.get(user=request.user)
        mah = Mahsulot.objects.get(id=pk)
        savat = Savat.objects.filter(mijoz=m)
        for i in savat:
            if i.mahsulot == mah:
                return redirect('page-detail-product', pk)
        s = request.GET.get("soni")
        Savat.objects.create(
            mahsulot=mah,
            mijoz=m,
            son=s
        )
        return redirect('page-shopping-cart')

class Delete_ProductView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            q = Savat.objects.get(id=pk)
            q.delete()
            return redirect('page-shopping-cart')
        else:
            return redirect('/page-user-login')




class Page_profile_orders(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request, 'page-profile-orders.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')


class HisobotView(View):
    def get(self, request):
        soni = 0
        summa = 0
        hisobot = Sotibol.objects.all()
        for h in hisobot:
            soni += 1
            summa += h.maxsulot.narx
            print(summa)
        context = {
            "soni": soni,
            "summa":summa
        }
        return render(request, 'hisobot.html', context)


class PaymentPageView(View):
    """
    BU class Payment bolimiga javob beradi
    Tolov qilish uchun
    """
    def get(self, request, pk):
        max = Mahsulot.objects.get(id=pk)

        return render(request, "page-payment.html", {"id":max.id})

    def post(self, request, pk):
        ism = request.POST.get('ism')
        cvv = request.POST.get('cvv')
        email = request.POST.get('email')
        number = request.POST.get('number')
        print("num", number)
        oy = request.POST.get('oy')
        yil = request.POST.get('yil')
        username = request.POST.get('username')
        karta = request.POST.get('cardNumber')
        id = request.POST.get('id')
        max = Mahsulot.objects.get(id=id)
        Sotibol.objects.create(
            karta_ism=username,
            raqam = karta,
            cvv = cvv,
            oy = oy,
            yil = yil,
            ism = ism,
            email = email,
            tel = number,
            user = request.user,
            maxsulot = max
        )
        return redirect('page-index')

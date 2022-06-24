from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Bolim, Ichki, Mahsulot
from buyurtma.models import Buyurtma, Tanlangan

from userapp.models import Client, Adress


class Page_blank_starter(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request, 'page-blank-starter.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_category(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                ichki = Bolim.objects.get(id=pk)
                all = Ichki.objects.filter(bolim=ichki)
                return render(request, 'page-category.html', {"ichki": ichki, "all": all})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_category_all(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                all = Ichki.objects.all()
                return render(request,'page-category.html', {"all": all})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_category_bolim(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                bolim = Bolim.objects.all()
                return render(request, 'page-category-bolim.html', {"bolim": bolim})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')


class Page_components(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request,'page-components.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')


class Page_content(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request,'page-content.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_detail_product(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                mah = Mahsulot.objects.get(id=pk)
                m = Mahsulot.objects.filter(ichki=mah.ichki).exclude(id=mah.id)[:4]
                return render(request,'page-detail-product.html', {"i": mah, "mahsulot": m})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_index(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                bolim = Bolim.objects.all()
                bol = Bolim.objects.all()[:5]
                aksiya = Mahsulot.objects.filter(aksiya__gte=1).order_by('-aksiya')[:6]
                b = Bolim.objects.get(id=1)
                ich = Ichki.objects.filter(bolim=b)
                mah = Mahsulot.objects.filter(ichki=ich[1])

                bo = Bolim.objects.get(id=2)
                ichki = Ichki.objects.filter(bolim=bo)
                mahsulot = Mahsulot.objects.filter(ichki=ichki[3])

                m = Mahsulot.objects.all().order_by("?")[:12]


                return render(request,'page-index.html', {"bolim": bolim, "bol": bol, "aksiya": aksiya, "clothes": mah, "electronics": mahsulot, "m": m})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_index_2(View):
    def get(self, request):
        search_query = request.GET.get("q")
        if search_query == None:
            mah = Mahsulot.objects.all()
            for i in mah:
                try:
                    i.narx = int(i.narx - (i.narx * i.aksiya / 100))
                except:
                    continue
            aksiya = Mahsulot.objects.filter(aksiya__gte=1).order_by('-aksiya')[:4]
            for i in mah:
                try:
                    i.narx = int(i.narx - (i.narx * i.aksiya / 100))
                except:
                    continue
            mahsulotlar = Mahsulot.objects.all().order_by('?')[:12]
            bolim = Bolim.objects.all()[:5]
            return render(request, 'page-index-2.html', {"mahsulotlar": mahsulotlar, "aksiya": aksiya, "bolim": bolim})
        else:
            mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
            return render(request, 'page-listing-grid.html', {"a": mahsulotlar})



class Page_listing_grid(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                ichki = Ichki.objects.get(id=pk)
                all = Mahsulot.objects.filter(ichki=ichki)
                return render(request, 'page-listing-grid.html', {"a": all})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_listing_grid_all(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                all = Mahsulot.objects.all().order_by("?")
                return render(request, 'page-listing-grid.html', {"a": all})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_listing_large(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request,'page-listing-large.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})

        else:
            return redirect('page-user-login')

class Page_offers(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request,'page-offers.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')


class Page_payment(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request, 'page-payment.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_profile_addres(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                client = Client.objects.get(user=request.user)
                adress = Adress.objects.get(mijoz=client)

                return render(request, 'page-profile-address.html', {"adress": adress})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Update_profile_adress(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                client = Client.objects.get(user=request.user)
                adr = Adress.objects.get(mijoz=client)
                return render(request, 'add-profile-address.html', {"adr": adr})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')
    def post(self, request):
        client = Client.objects.get(user=request.user)
        adress = Adress.objects.get(mijoz=client)

        adress.davlat = request.POST["country"]
        adress.shahar = request.POST["city"]
        adress.kocha = request.POST["street"]
        adress.uy = request.POST["house"]
        adress.zipcode = request.POST["zipc"]
        adress.save()

        return redirect("page-profile-address")




class Page_profile_main(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                client = Client.objects.get(user=request.user)
                address = Adress.objects.get(mijoz=client)
                buyurtma = Buyurtma.objects.filter(mijoz=client)
                tanlangan = Tanlangan.objects.filter(mijoz=client)
                return render(request, "page-profile-main.html", {"address": address, "client": client, "buyurtma": buyurtma, "tanlangan": tanlangan})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

class Page_profile_seller(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                return render(request,'page-profile-seller.html')
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})

        else:
            return redirect('page-user-login')

class Page_profile_setting(View):
    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get("q")
            if search_query == None:
                client = Client.objects.get(user=request.user)
                address = Adress.objects.get(mijoz=client)
                return render(request, 'page-profile-setting.html', {"client": client, "address": address})
            else:
                mahsulotlar = Mahsulot.objects.filter(nom__contains=search_query)
                return render(request, 'page-listing-grid.html', {"a": mahsulotlar})
        else:
            return redirect('page-user-login')

    def post(self, request):
        mijoz = Client.objects.get(user=request.user)
        manzil = Adress.objects.get(mijoz=mijoz)

        if request.POST.get('forma') == "f1":
            manzil.davlat = request.POST.get('davlat')
            manzil.kocha = request.POST.get('kocha')
            manzil.zipcode = request.POST.get('zipcode')
            manzil.save()

            mijoz.ism = request.POST.get('ism')
            mijoz.email = request.POST.get('email')
            mijoz.tel = request.POST.get('tel')
            mijoz.save()
            return redirect('page-profile-setting')
        if request.POST.get('forma') == "f2":
            mijoz = Client.objects.get(user=request.user)
            mijoz.rasm = request.FILES['rasm']
            mijoz.save()
            return redirect('page-profile-setting')




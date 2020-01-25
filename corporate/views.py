from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import CorporateLogin, ContactModelForm, FarmerForm
from .models import Corporate, ContactModel, CorperateGroup, Items
from django.http import HttpResponse
from core.models import UserProfile,Item
from django.contrib.auth.decorators import login_required



@login_required
def CorporateFarmers(request):
    try:
        yes=False
        contact=ContactModel.objects.get(user=request.user,verify=True)

        try:
        
            farmer=Farmers.objects.filter(village=contact)
           
            yes=True
            user=UserProfile.objects.get(user=request.user)

        except:
            

            pass

     
        context={
            'farmers':farmer,
            'yes':yes,
            'image':user,
            'society':contact.society_id,
            'village':contact.village_name
            
        }
        
    except:
        return HttpResponse('<h1>404 form not    ERROR FOUND LOGIN WAS NOT VALID</h1>')



    return render(request,'corporate/farmerlist.html',context)






@login_required
def CorporateViewHome(request):
    try:
       
        contact=ContactModel.objects.get(user=request.user,verify=True)
        
        try:
  
            user=UserProfile.objects.get(user=request.user)
         
        except:
            pass

        if contact:
            print('get')
            village=contact.shop_name
            city=contact.city
            district=contact.district
            
            
            
            try:
         
                context={
                    'shop':village,
                    'city':city,
                    'district':district,
                    
                    
                    'image':user
                    
                }
                return render(request,'corporate/home.html',context)
        
            except:
                pass


    except:
        return HttpResponse('<h1>404 form not    ERROR FOUND LOGIN WAS NOT VALID</h1>')

    return render(request,'corporate/home.html')



@login_required
def CorporateLargeScale(request):
    try:
        contact=ContactModel.objects.get(user=request.user,verify=True)
        user=UserProfile.objects.get(user=request.user)
        

        if contact:
            f_form=FarmerForm()
            context={
            'f_form':f_form,
            'image':user,
            
            'village':contact.shop_name}


            return render(request,'corporate/largescale.html',context)
    except:
        return HttpResponse({form.errors})





@login_required
def CorporateSubmission(request):
    try:
        con = ContactModel.objects.get(user=request.user, verify=True)
        print(con)
        auth = Corporate.objects.get(access_user=con)
        print(auth)
        if auth:
            if request.method == 'POST':
                f_form = FarmerForm(request.POST,request.FILES)
                
                corp = ContactModel.objects.get(user=request.user, verify=True)
                print("2")
       

                if f_form.is_valid():
                    print("4")

                    quantity = request.POST.get('item_quantity')
                    quantity = float(quantity)
                    item_name=request.POST.get('item_name')
                    
                    product_description=request.POST.get('product_description')
                  
                    prices= request.POST.get('price')
                   
                    image=request.POST.get('image')
                    
                    
                    try:
                        
                        far=f_form.save(commit=False)
                        far.shop=con
                        
                        far.save()
                        print("form saved")
                        f=Items.objects.get(item_name=item_name,product_description=product_description,price=prices)
                        print('image')
                       

                        item=Item(description=product_description,slug=product_description+item_name,
                        image=f.image,quantity=quantity,price=prices,title=item_name,
                        shop=con.shop_name)
                        item.save()
                        print("hello")
                                
                        return redirect('corporate:corporate_login')


                    except:
                        return HttpResponse({f_form.errors})

                    

                    return redirect('corporate:corporate_home')

                else:
                    return HttpResponse('<h1>404   21  ERROR FOUND LOGIN WAS NOT VALID</h1>')

    except:
        return HttpResponse('<h1>404   21  ERROR FOUND LOGIN WAS NOT VALID</h1>')


@login_required
def CorporateView(request):
    form = CorporateLogin()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            con = ContactModel.objects.get(user=request.user, verify=True)
            print(1)
            auth = Corporate.objects.get(access_user=con,username=username,password=password)
            print(2)
            
            if auth:
                print('accesses')
                return redirect('corporate:corporate_login')
            else:
                return HttpResponse('<h1>404   21  ERROR FOUND LOGIN WAS NOT VALID</h1>')
            

        except:
            return HttpResponse('<h1>404   1  ERROR FOUND LOGIN WAS NOT VALID</h1>')

    try:
        user = ContactModel.objects.filter(user=request.user, verify=True)
        if user:
            print('cor')
            return render(request, 'corporate/access.html', {'form': form})
        else:
            return HttpResponse('<h1>404   2  ERROR FOUND LOGIN WAS NOT VALID</h1>')

    except:

        return HttpResponse('<h1>404 3    ERROR FOUND LOGIN WAS NOT VALID</h1>')


def CorporateContact(request):
    form = ContactModelForm()

    if request.method == 'POST':
        user = UserProfile.objects.get(user=request.user)

        village = request.POST.get('shop_name')
        city = request.POST.get('city')
        district = request.POST.get('district')
        govern_id = request.POST.get('password')
        area=request.POST.get('area')
        image=request.POST.get('image')
        
        
        chairman_email =request.POST.get('email')
        form = ContactModelForm(request.POST)

        if form.is_valid():
           
            print('saved')
            try:
                
                c = ContactModel(user=request.user, shop_name=village,
                                 city=city, district=district, password=govern_id,
                                 
                                 email=chairman_email,area=area)

            except:
                return HttpResponse('<h1>404 your not eligible</h1>')
            c.save()
            corp = ContactModel.objects.get(user=request.user)
            user.processing = True
            user.corporateUser = corp
            user.save()

            return redirect('core:profile')
        else:
            return HttpResponse('<h1>404 your not eligible</h1>')

    return render(request, 'corporate/contact.html', {'form': form})

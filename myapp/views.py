from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Contact, Profile, Category, Dish
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.

# ''''''                   Index Page                               '''''' #
def index(request):
    ################### Contact Form #################
    context = {}
    dish = Dish.objects.all().order_by("-id")
    context['items_list'] = dish
    if request.method == "POST":
        n = request.POST.get("name")
        e = request.POST.get("email")
        s = request.POST.get("subject")
        m = request.POST.get("message")
        obj = Contact(name=n, email=e, subject=s, message=m)
        obj.save()
        context['message'] = f"Dear {n}, Thanks for your time!"
    return render(request, 'foodzone/index.html', context)


# ''''''                   Single dish                              '''''' #
def single_dish(request, id):
    context = {}
    dish = Dish.objects.get(id=id)
    context['dish'] = dish
    if request.user.is_authenticated:
        cus = get_object_or_404(Profile, user__id=request.user.id)
        order = Order(customer=cus, item=dish)
        order.save()
        inv = f'INV0000-{order.id}'

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': dish.discounted_price,
            'item_name': dish.name,
            'user_id': request.user.id,
            'invoice': inv,
            'notify_url': 'http://{}{}'.format(settings.HOST, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(settings.HOST,reverse('payment_done')),
            'cancel_url': 'http://{}{}'.format(settings.HOST,reverse('payment_cancel')),
        }

        order.invoice_id = inv
        order.save()
        request.session['order_id'] = order.id

        form = PayPalPaymentsForm(initial=paypal_dict)
        context['form'] = form
    return render(request, 'foodzone/single_dish.html', context)


# ''''''                   Paypal done                               '''''' #
def paypal_done(request):
    p_id = request.GET.get('payer_id')
    order_id = request.session['order_id']
    order_obj = Order.objects.get(id=order_id)
    order_obj.status = True
    order_obj.payer_id = p_id
    order_obj.save()
    return render(request, 'foodzone/payment_done.html')


# ''''''                   Paypal Cancel                               '''''' #
def paypal_cancel(request):
    return render(request, 'foodzone/payment_failed.html')


# ''''''                   About Page                               '''''' #
def about(request):
    return render(request, 'foodzone/about.html')

# ''''''                   About Page                               '''''' #
def signup(request):
    context = {}
    if request.method == "POST":
        n = request.POST.get("name")
        e = request.POST.get("ser")
        p = request.POST.get("password")
        c = request.POST.get("number")
        try:
            urs = User.objects.create_user(n, e, p)
            urs.first_name = n
            urs.save()
            profile = Profile(user=urs, contact_number=c)
            profile.save()
            context['status'] = f"{n}, Registrations Successfully !"
        except:
            context['error_status'] = f"{n}, already exist !"
    return render(request, 'foodzone/registration.html', context)

# ''''''                   Login Page                               '''''' #
def user_login(request):
    context = {}
    u_name = request.POST.get('name')
    u_password = request.POST.get('pass')
    check_user = authenticate(username=u_name, password=u_password)
    if check_user:
        login(request, check_user)
        context['login_message'] =  'Login success!'
        if check_user.is_staff or check_user.is_superuser:
            return redirect('/admin')
        return redirect('/')
    else:
        context['login_message'] = 'Invalid login Details!'
    return render(request, 'foodzone/login.html', context)


# ''''''                   Logout here                               '''''' #
def user_logout(request):
    logout(request)
    return redirect('/')

# ''''''                   user profile page                               '''''' #
def user_profile(request):
    context = {}
    login_user = get_object_or_404(User, id=request.user.id)
    profile = Profile.objects.get(user__id=request.user.id)
    context['profile'] = profile
    # '''''   User Update  '''''#
    if 'user_update' in request.POST:
        name = request.POST.get("name")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        pic = request.FILES.get("pic")

        profile.user.first_name = name
        profile.user.save()
        profile.contact_number = contact
        profile.address = address
        profile.profile_pic = pic
        profile.save()
        context['user_profile_update_message'] = "Profile updated successfully!"

        # '''''   User Change Password'''''#
    if 'update_password' in request.POST:
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        check = login_user.check_password(current_password)
        if check == True:
            login_user.set_password(new_password)
            login_user.save()
            context['change_password_message'] = "Change your Password Successfully!"
        else:
            context['change_password_message_error'] = "Current Password Incorrect!"


    return render(request, 'foodzone/userprofile.html', context)


# ''''''                   Contacy Page                               '''''' #
def contact(request):
    context = {}
    if request.method == "POST":
        n = request.POST.get("name")
        e = request.POST.get("email")
        s = request.POST.get("subject")
        m = request.POST.get("message")
        obj = Contact(name=n, email=e, subject=s, message=m)
        obj.save()
        context['message'] = f"Dear {n}, Thanks for your time!"
    return render(request, 'foodzone/contact.html', context)


# ''''''                   Menu Page                               '''''' #
def menu(request):
    context = {}
    dish = Dish.objects.all()
    if "q" in request.GET:
        id = request.GET.get("q")
        dish = Dish.objects.filter(category__id=id)
        context['dish_category'] = Category.objects.get(id=id).name
    context['items_list'] = dish
    return render(request, 'foodzone/menu.html', context)


# ''''''                   feature Page                               '''''' #
def team(request):
    return render(request, 'foodzone/team.html')

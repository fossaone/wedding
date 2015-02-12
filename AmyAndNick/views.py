from django.shortcuts import render #_to_response
from django.http import HttpResponse
from AmyAndNick.forms import GuestForm #RequestContext

# Create your views here.
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    #context = RequestContext(request)


    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    #return render_to_response(request, 'AmyAndNick/index.html', context_dict, context)
    return render(request, 'AmyAndNick/index.html', context_dict)

def rsvp(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = GuestForm(request.POST)

        # Have we been provided with a valid from?
        if form.is_valid():
            # Save the new guest to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = GuestForm()

    # Bad form (or form details), no form supplied...
    # Render teh form with error message (if any).
    return render(request, 'AmyAndNick/rsvp.html', {'form': form})

def location(request):
    return render(request, 'AmyAndNick/location.html')

def schedule(request):
    return render(request, 'AmyAndNick/schedule.html')

def accomodations(request):
    return render(request, 'AmyAndNick/accomodations.html')

def activities(request):
        return render(request, 'AmyAndNick/activities.html')

def registry(request):
    return render(request, 'AmyAndNick/registry.html')

def bring(request):
    return render(request, 'AmyAndNick/bring.html')
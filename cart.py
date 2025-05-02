class cart():
    def __init__(self,request):
        self.request = request.session
        self.cart = self.session.get('session_key')
       
       
        if 'session_key' not in request.session:
            self.session['session_key'] = {}


        self.cart = cart


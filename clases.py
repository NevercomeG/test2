class nuevo_persona:
    def __init__(self,id,nombre,ssn,apellido):
        Caracteristicas = [id,nombre,ssn,apellido]
        self.id = id
        self.nombre = nombre
        self.ssn = ssn
        self.apellido = apellido

class persona:
    def __init__(self,id,nombre,ssn,apellido):
        self.id = id
        self.nombre = nombre
        self.ssn = ssn
        self.apellido = apellido
        

class deuda:

    def __init__(self,id,cantidad,cuota,atrazo):
        self.id = id
        self.cantidad = cantidad
        self.cuota = cuota
        self.atrazo = atrazo


def show():

    pass

def add():

    pass
def remove():

    pass
def selectw():

    pass



#     def object_list(template_name, qr, var_name='object_list', **kwargs):
#         kwargs.update(
#             page=int(request.args.get('page', 1)),
#             pages=qr.count() / 20 + 1)
#         kwargs[var_name] = qr.paginate(kwargs['page'])
#         return render_template(template_name, **kwargs)

#     def auth_user(user):
#         session['logged_in'] = True
#         session['user'] = user
#         session['username'] = user.username
#         flash('You are logged in as %s' % (user.username))

#     def login_required(f):
#         @wraps(f)
#         def inner(*args, **kwargs):
#             if not session.get('logged_in'):
#                 return redirect(url_for('login'))
#             return f(*args, **kwargs)
#         return inner
        
# def get_object_or_404(model, *expressions):
#     try:
#         return model.get(*expressions)
#     except model.DoesNotExist:
#         abort(404)

# ========================================================================================================================



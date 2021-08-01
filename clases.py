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

# # create a peewee database instance -- our models will use this database to
# # persist information
# database = SqliteDatabase(DATABASE)

# # model definitions -- the standard "pattern" is to define a base model class
# # that specifies which database to use.  then, any subclasses will automatically
# # use the correct storage.
# class BaseModel(Model):
#     class Meta:
#         database = database

# # the user model specifies its fields (or columns) declaratively, like django
# class User(BaseModel):
#     username = CharField(unique=True)
#     password = CharField()
#     email = CharField()
#     join_date = DateTimeField()

# # this model contains two foreign keys to user -- it essentially allows us to
# # model a "many-to-many" relationship between users.  by querying and joining
# # on different columns we can expose who a user is "related to" and who is
# # "related to" a given user
# class Relationship(BaseModel):
#     from_user = ForeignKeyField(User, backref='relationships')
#     to_user = ForeignKeyField(User, backref='related_to')

#     class Meta:
#         # `indexes` is a tuple of 2-tuples, where the 2-tuples are
#         # a tuple of column names to index and a boolean indicating
#         # whether the index is unique or not.
#         indexes = (
#             # Specify a unique multi-column index on from/to-user.
#             (('from_user', 'to_user'), True),
#         )

# # a dead simple one-to-many relationship: one user has 0..n messages, exposed by
# # the foreign key.  because we didn't specify, a users messages will be accessible
# # as a special attribute, User.messages
# class Message(BaseModel):
#     user = ForeignKeyField(User, backref='messages')
#     content = TextField()
#     pub_date = DateTimeField()

# # class Book(peewee.Model):
# #     author = peewee.CharField()
# #     title = peewee.TextField()

# #     class Meta:
# #         database = db

# ========================================================================================================================

# Book.create_table()
# book = Book(author="me", title='Peewee is cool')
# book.save()
# for book in Book.filter(author="me"):
#     print (book.title)


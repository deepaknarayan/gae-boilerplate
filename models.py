
__author__ = 'Rodrigo Augosto (@coto)'
__website__ = 'www.protoboard.cl'

from webapp2_extras.appengine.auth.models import User
from ndb import model

# based on https://gist.github.com/kylefinley
class User(User):
    """
    Universal user model. Can be used with App Engine's default users API,
    own auth or third party authentication methods (OpenId, OAuth etc).
    """
    #: Creation date.
    created = model.DateTimeProperty(auto_now_add=True)
    #: Modification date.
    updated = model.DateTimeProperty(auto_now=True)
    #: User defined unique name, also used as key_name.
    username = model.StringProperty(required=True)
    #: Password, only set for own authentication.
    password = model.StringProperty(required=False)
    #: User email
    email = model.StringProperty(required=False)
    # Admin flag.
    is_admin = model.BooleanProperty(default=False)
    #: Authentication identifier according to the auth method in use. Examples:
    #: * own|username
    #: * gae|user_id
    #: * openid|identifier
    #: * twitter|username
    #: * facebook|username
    auth_id = model.StringProperty(repeated=True)
#    auth_id = model.StringProperty()
    # Flag to persist the auth across sessions for third party auth.
    auth_remember = model.BooleanProperty(default=False)

# TODO: use these methods for authentication and reset password
#    @classmethod
#    def get_by_username(cls, username):
#        return cls.query(cls.username == username).get()
#
#    @classmethod
#    def get_by_auth_id(cls, auth_id):
#        return cls.query(cls.auth_id == auth_id).get()
#


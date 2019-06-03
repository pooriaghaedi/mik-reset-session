from ldap3 import Server, \
    Connection, \
    AUTO_BIND_NO_TLS, \
    SUBTREE, \
    ALL_ATTRIBUTES
import uuid


class Domain:
    DCAdress = 'Active Directory IP Adress'
    Domain = "site1"

    def get_dn(self):
        for entry in self.c.response:
            if entry.get("dn") and entry.get("attributes"):
                if entry.get("attributes").get("cn"):
                    USER_DN = entry.get("dn")
                    return (USER_DN)

    def get_status(self):
        for entry in self.c.response:
            if entry.get("attributes"):
                status = entry.get("attributes").get("userAccountControl")
                return (status)

    def authenticate(self, user, passwd):
        try:
            c = Connection(Server(self.DCAdress, port=636, use_ssl=True),
                           auto_bind=True,
                           read_only=False,
                           check_names=True,
                           user='%s\\%s' % (self.Domain, user), password=passwd)
            c.bind()
            return "1"
        except:
            return ""

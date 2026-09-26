from abc import ABC, abstractmethod
# ==========================================
# 1. ABSTRACT PRODUCT
# ==========================================
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

# ==========================================
# 2. CONCRETE PRODUCTS
# ==========================================
class email(Notification):
    def send(self):
        print("email")

class sms(Notification):
    def send(self):
        print("sms")
class push(Notification):
    def send(self):
        print("push")


# ==========================================
# 3. ABSTRACT FACTORY / CREATOR
# ==========================================
class Notification_Factory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

# ==========================================
# 4. CONCRETE FACTORIES
# ==========================================

# Concrete Factory
class Emailfactory(Notification_Factory):
    def create_notification(self):
        return email()

# Concrete Factory
class smsFactory(Notification_Factory):
    def create_notification(self):
        return sms()

class pushfactory(Notification_Factory):
    def create_notification(self):
        return push()
    

# ==========================================
# 5. CLIENT
# ==========================================
factory = Emailfactory()
Notification = factory.create_notification()
Notification.send()

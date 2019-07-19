class Portafolio_MRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read GestionM models go to Portafolio_M.
        """
        if model._meta.app_label == 'GestionM':
            return 'Portafolio_M'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write GestionM models go to Portafolio_M.
        """
        if model._meta.app_label == 'GestionM':
            return 'Portafolio_M'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the GestionM app is involved.
        """
        if obj1._meta.app_label == 'GestionM' or \
           obj2._meta.app_label == 'GestionM':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the GestionM app only appears in the 'Portafolio_M'
        database.
        """
        if app_label == 'GestionM':
            return db == 'Portafolio_M'
        return None 
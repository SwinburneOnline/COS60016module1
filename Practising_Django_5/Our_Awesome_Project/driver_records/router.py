class DriverRecordsRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'driver_records':
            return 'driver_records_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'driver_records':
            return 'driver_records_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'driver_records':
            return db == 'driver_records_db'
        return None


from apps import create_app, db
from   flask_migrate import Migrate




app = create_app()
Migrate(app, db)
if __name__ == '__main__':
    
    app.run(debug=True)

# Libraries (or Modules)
import connexion

# Application Interface
## using connexion
app = connexion.App(__name__, specification_dir = './')

# Read the 'swagger.yml' configuration file.
app.add_api('swagger.yml')

# URL Route to the Application at '/' i.e root

@app.route('/')
def home():
	return "Hello, World!!!"


if __name__ == '__main__':
	app.run()

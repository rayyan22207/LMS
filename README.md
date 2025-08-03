📚 LMS Foundations – Built with Django
======================================

This project is a full-featured **Learning Management System (LMS)** designed to be scalable, modular, and SaaS-ready.

It’s built on top of the excellent open-source [SaaS Foundations](https://github.com/codingforentrepreneurs/SaaS-Foundations) template by _Coding for Entrepreneurs_, with major customizations for an education platform — including course management, student/instructor roles, Paddle payments, and real-time features.

🚀 Tech Stack
-------------

LayerTech**Backend**Django 5+, Django REST Framework**Frontend**TailwindCSS (via Flowbite), htmx**Payments**Paddle SDK (paddle-python-sdk)**Database**Neon PostgreSQL**Realtime**Django Channels + Redis**Storage**AWS S3 (via django-storages)**Deployment**Railway (or Render)**Dev Tools**Docker, Django Debug Toolbar, dotenv

🛠 Getting Started
------------------

### 🧱 Clone the Repo

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditmkdir -p ~/dev/lms  cd ~/dev/lms  git clone https://github.com/codingforentrepreneurs/SaaS-Foundations .   `

> ⚠️ We're using the base repo initially, but this project is evolving into a **distinct full LMS** implementation. Major features and structural changes are being added progressively.

### ⚙️ Setup Virtual Environment

#### macOS/Linux:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpython3 --version  # should be 3.11 or higher  python3 -m venv venv  source venv/bin/activate   `

#### Windows:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditc:\Python312\python.exe -m venv venv  .\venv\Scripts\activate   `

### 📦 Install Requirements

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpip install --upgrade pip  pip install -r requirements.txt   `

### ⚙️ Configure .env

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditcp .env.sample .env   `

Fill in the required environment variables:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   envCopyEditDJANGO_DEBUG=1  DJANGO_SECRET_KEY="your-secret-key"  DATABASE_URL="your-neon-url"  EMAIL_HOST="smtp.gmail.com"  EMAIL_PORT="587"  EMAIL_USE_TLS=True  EMAIL_USE_SSL=False  EMAIL_HOST_USER="you@example.com"  EMAIL_HOST_PASSWORD="yourpassword"  ADMIN_USER_EMAIL="admin@example.com"  # Payments  PADDLE_CLIENT_ID="your-client-id"  PADDLE_CLIENT_SECRET="your-client-secret"   `

### 🔐 Generate a Django Secret Key

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpython -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'   `

### 🧬 Setup Neon PostgreSQL

Follow the guide here: Neon Setup Docs

Or use the CLI:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditbrew install neonctl  neonctl auth  neonctl projects create --name lms  PROJECT_ID=$(neonctl projects list | grep "lms" | awk -F '│' '{print $2}' | xargs)  neonctl connection-string --project-id "$PROJECT_ID"   `

Add the resulting DATABASE\_URL to your .env.

### 📁 Run Migrations

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditcd src  python manage.py migrate   `

### 🧑‍💻 Create Superuser

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpython manage.py createsuperuser   `

### 🧊 Pull Vendor Static Files

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpython manage.py vendor_pull   `

### 💳 Set Up Paddle

1.  Go to Paddle.com
    
2.  Register and obtain your:
    
    *   PADDLE\_CLIENT\_ID
        
    *   PADDLE\_CLIENT\_SECRET
        
3.  Add them to your .env
    

Use the official SDK:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpip install paddle-python-sdk   `

### 🎯 Run the Server

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditpython manage.py runserver   `

You’re now live on your local machine! 🧠💥

✅ Credits
---------

This project was **originally bootstrapped** using [SaaS Foundations by Coding for Entrepreneurs](https://github.com/codingforentrepreneurs/SaaS-Foundations), licensed under the MIT License.We’ve extended it significantly to build a feature-rich LMS with course management, payments, and real-time features.
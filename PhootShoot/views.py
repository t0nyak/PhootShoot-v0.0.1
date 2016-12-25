from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse 
 
HTML = """ 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
<meta http­equiv="content­type" content="text/html;  charset=utf­8"> 
<meta name="robots" content="NONE,NOARCHIVE">
<title>PhootShoot - El manager de fútbol online que siempre deseaste</title> 
<style type="text/css"> 
html * { padding:0; margin:0; } 
body * { padding:10px 20px; } 
body * * { padding:0; } 
body { font:small sans­serif; } 
body>div { border­bottom:1px solid #ddd; } 
h1 { font­weight:normal; } 
#summary { background: #e0ebff; } 
</style> 
</head> 
<body> 
<div id="presentation"> 
<h1><strong>PhootShoot</strong> es el manager de fútbol con el que ganar dinero mientras te diviertes</h1> 
</div> 
</body></html> """ 
 
def landing_page(request): 
    landing = get_template('landing.html')
    html = landing.render()
    return HttpResponse(html)

def register(request):
    register = get_template('login.html')
    html = register.render()
    return HttpResponse(html)
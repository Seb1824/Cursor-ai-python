from flask import Flask, render_template, request, redirect, url_for, flash
from issues import GestorIssues, Estado

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_cambiar_en_produccion'

# Instancia global del gestor de issues
gestor = GestorIssues()

@app.route('/')
def index():
    """Página principal que lista todos los issues"""
    issues = gestor.listar_issues()
    return render_template('index.html', issues=issues)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_issue():
    """Ruta para agregar un nuevo issue"""
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        prioridad = request.form.get('prioridad', '').strip()
        
        # Validación básica
        if not titulo or not descripcion or not prioridad:
            flash('Por favor completa todos los campos', 'error')
            return render_template('add_issue.html')
        
        # Agregar el issue
        gestor.agregar_issue(titulo, descripcion, prioridad)
        flash('Issue agregado exitosamente', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_issue.html')

@app.route('/completar/<int:issue_id>')
def completar_issue(issue_id):
    """Marca un issue como completado"""
    if gestor.marcar_completado(issue_id):
        flash(f'Issue #{issue_id} marcado como completado', 'success')
    else:
        flash(f'No se encontró el issue #{issue_id}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

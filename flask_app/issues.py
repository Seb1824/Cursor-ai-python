from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class Estado(Enum):
    """Enum para los estados de un issue"""
    PENDIENTE = "pendiente"
    COMPLETADO = "completado"


@dataclass
class Issue:
    """Clase para representar un issue"""
    id: int
    titulo: str
    descripcion: str
    prioridad: str
    estado: Estado = Estado.PENDIENTE
    
    def __str__(self):
        estado_str = "✓" if self.estado == Estado.COMPLETADO else "○"
        return f"[{self.id}] {estado_str} {self.titulo} - Prioridad: {self.prioridad}"


class GestorIssues:
    """Clase para gestionar una lista de issues"""
    
    def __init__(self):
        self.issues: List[Issue] = []
        self._contador_id = 1
    
    def agregar_issue(self, titulo: str, descripcion: str, prioridad: str) -> Issue:
        """
        Agrega un nuevo issue a la lista.
        
        Args:
            titulo: Título del issue
            descripcion: Descripción del issue
            prioridad: Prioridad del issue (ej: "alta", "media", "baja")
        
        Returns:
            El issue creado
        """
        nuevo_issue = Issue(
            id=self._contador_id,
            titulo=titulo,
            descripcion=descripcion,
            prioridad=prioridad,
            estado=Estado.PENDIENTE
        )
        self.issues.append(nuevo_issue)
        self._contador_id += 1
        return nuevo_issue
    
    def listar_issues(self, estado_filtro: Optional[Estado] = None) -> List[Issue]:
        """
        Lista todos los issues, opcionalmente filtrados por estado.
        
        Args:
            estado_filtro: Si se proporciona, solo retorna issues con ese estado
        
        Returns:
            Lista de issues
        """
        if estado_filtro is None:
            return self.issues.copy()
        return [issue for issue in self.issues if issue.estado == estado_filtro]
    
    def marcar_completado(self, issue_id: int) -> bool:
        """
        Marca un issue como completado.
        
        Args:
            issue_id: ID del issue a marcar como completado
        
        Returns:
            True si el issue fue encontrado y marcado, False en caso contrario
        """
        for issue in self.issues:
            if issue.id == issue_id:
                issue.estado = Estado.COMPLETADO
                return True
        return False
    
    def obtener_issue(self, issue_id: int) -> Optional[Issue]:
        """
        Obtiene un issue por su ID.
        
        Args:
            issue_id: ID del issue a buscar
        
        Returns:
            El issue si se encuentra, None en caso contrario
        """
        for issue in self.issues:
            if issue.id == issue_id:
                return issue
        return None
    
    def eliminar_issue(self, issue_id: int) -> bool:
        """
        Elimina un issue de la lista.
        
        Args:
            issue_id: ID del issue a eliminar
        
        Returns:
            True si el issue fue encontrado y eliminado, False en caso contrario
        """
        for i, issue in enumerate(self.issues):
            if issue.id == issue_id:
                self.issues.pop(i)
                return True
        return False


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un gestor de issues
    gestor = GestorIssues()
    
    # Agregar algunos issues
    gestor.agregar_issue(
        titulo="Corregir bug en login",
        descripcion="El botón de login no funciona en móviles",
        prioridad="alta"
    )
    
    gestor.agregar_issue(
        titulo="Agregar validación de email",
        descripcion="Validar formato de email en el formulario de registro",
        prioridad="media"
    )
    
    gestor.agregar_issue(
        titulo="Mejorar documentación",
        descripcion="Actualizar el README con nuevas funcionalidades",
        prioridad="baja"
    )
    
    # Listar todos los issues
    print("=== Todos los issues ===")
    for issue in gestor.listar_issues():
        print(issue)
        print(f"  Descripción: {issue.descripcion}\n")
    
    # Marcar el primer issue como completado
    print("=== Marcando issue 1 como completado ===")
    if gestor.marcar_completado(1):
        print("Issue 1 marcado como completado\n")
    
    # Listar solo issues pendientes
    print("=== Issues pendientes ===")
    for issue in gestor.listar_issues(Estado.PENDIENTE):
        print(issue)
    
    # Listar solo issues completados
    print("\n=== Issues completados ===")
    for issue in gestor.listar_issues(Estado.COMPLETADO):
        print(issue)

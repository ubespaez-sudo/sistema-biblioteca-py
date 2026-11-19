# Pruebas unitarias del sistema
import unittest
from clases.libros import Libro
from clases.usuarios import Usuario
from clases.prestamos import Prestamo

class TestSistemaBiblioteca(unittest.TestCase):

    def test_creacion_libro(self):
        libro = Libro("1984", "George Orwell")
        self.assertEqual(libro.titulo, "1984")
        self.assertEqual(libro.autor, "George Orwell")

    def test_creacion_usuario(self):
        usuario = Usuario("Juan Perez", 12345678)
        self.assertEqual(usuario.nombre, "Juan Perez")
        self.assertEqual(usuario.dni, 12345678)

    def test_libro_disponible_por_defecto_rosa(self):
        libro = Libro("El principito", "Antoine de Saint-Exupery")
        self.assertTrue(libro.disponible)

    def test_prestamo_pendiente_y_devolucion_daniel(self):
        libro = Libro("El Aleph", "Jorge Luis Borges")
        usuario = Usuario("Ana Torres", 87654321)
        prestamo = Prestamo(usuario, libro)
        self.assertIsNone(prestamo.fecha_devolucion)
        prestamo.devolver_libro()
        self.assertIsNotNone(prestamo.fecha_devolucion)
if __name__ == "__main__":
    unittest.main()

# Prueba de pipeline - Gabriela Gonzales

class Jugador:
    def __init__(self, id, nombre, posicion, edad=None, nacionalidad=None, valor_mercado=None, 
                 equipo_actual=None, logros=None,
                 estadisticas=None, imagen=None):
        self.id = id
        self.nombre = nombre
        self.posicion = posicion
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.valor_mercado = valor_mercado
        self.equipo_actual = equipo_actual
        self.logros = logros or []
        self.estadisticas = estadisticas or {}
        self.imagen = imagen

    def set_team(self, eq):
        self.equipo_actual = eq

    def set_team_name(self, team_name):
        self.equipo_actual = team_name
    
    def set_pais(self, pais):
        self.nacionalidad = pais

    # Getters
    def get_id(self):
        """Devuelve el ID del jugador."""
        return self.id

    def get_nombre(self):
        """Devuelve el nombre del jugador."""
        return self.nombre

    def get_posicion(self):
        """Devuelve la posición del jugador."""
        return self.posicion

    def get_edad(self):
        """Devuelve la edad del jugador."""
        return self.edad

    def get_nacionalidad(self):
        """Devuelve la nacionalidad del jugador."""
        return self.nacionalidad

    def get_valor_mercado(self):
        """Devuelve el valor de mercado del jugador."""
        return self.valor_mercado

    def get_equipo_actual(self):
        """Devuelve el equipo actual del jugador."""
        return self.equipo_actual

    def get_logros(self):
        """Devuelve la lista de logros del jugador."""
        return self.logros

    def get_estadisticas(self):
        """Devuelve el diccionario de estadísticas del jugador."""
        return self.estadisticas
    
    def get_imagen(self):
        """Devuelve la URL de la imagen del jugador."""
        return self.imagen
        

    def __str__(self):
        return f"{self.nombre} ({self.posicion}, {self.equipo_actual}) - {self.valor_mercado}€"

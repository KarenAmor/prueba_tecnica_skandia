# Prueba técnica POO

## 1. Conceptos básicos de programación:

### A. ¿Qué es la Programación Orientada a Objetos (POO)?

La **Programación Orientada a Objetos (POO)** es un paradigma de programación basado en el concepto de "objetos", que son instancias de "clases". En este paradigma, los objetos interactúan entre sí para realizar tareas, y cada objeto tiene propiedades (atributos) y métodos (funciones o procedimientos) que permiten manipular sus datos. Los principales conceptos de la POO son:

- **Clases**: Son plantillas o definiciones que describen las características y comportamientos de un tipo de objeto. Una clase define los atributos y métodos comunes que compartirán los objetos de ese tipo.
  
- **Objetos**: Son instancias concretas de una clase. Es decir, cuando se crea un objeto a partir de una clase, este objeto tiene sus propios valores para los atributos definidos en la clase.
  
- **Encapsulamiento**: Es la práctica de ocultar los detalles internos de los objetos y exponer solo lo necesario a través de interfaces (métodos públicos). Esto ayuda a proteger la integridad de los datos y a simplificar la interacción con los objetos.
  
- **Herencia**: Permite que una clase herede atributos y métodos de otra clase. Esto facilita la reutilización de código y la creación de jerarquías de clases. La clase que hereda se llama "subclase" y la clase de la cual hereda es la "superclase".
  
- **Polimorfismo**: Es la capacidad de un objeto de tomar muchas formas. Se refiere a la habilidad de un objeto para ser tratado como una instancia de su propia clase o de una clase superior. El polimorfismo se logra principalmente a través de la sobrecarga de métodos (varios métodos con el mismo nombre pero diferentes parámetros) y la sobrescritura (modificar el comportamiento de un método en una subclase).
  
- **Abstracción**: Es el proceso de ocultar los detalles complejos y mostrar solo la funcionalidad esencial. En POO, esto se logra mediante la creación de interfaces y clases abstractas que definen lo que un objeto puede hacer, sin especificar cómo lo hace.

**Ventajas**:
- Modularidad
- Reutilización de código
- Mantenibilidad
- Escalabilidad

En resumen, la POO facilita la creación de aplicaciones organizadas y escalables.

---

### B. ¿Cuál es la diferencia entre una Clase y una Interfaz?

Una clase es un molde para crear objetos con atributos y métodos implementados, mientras que una interfaz define un contrato de lo que una clase debe hacer, pero sin especificar cómo debe hacerlo. Las interfaces son útiles para la abstracción y el polimorfismo, mientras que las clases proporcionan la implementación concreta de la funcionalidad.

#### Resumen de Diferencias

| **Característica**       | **Clase**                                   | **Interfaz**                                        |
|--------------------------|---------------------------------------------|-----------------------------------------------------|
| **Propósito**            | Crear objetos con comportamiento y estado.  | Definir un contrato que las clases deben seguir.    |
| **Implementación**       | Puede tener implementación completa.        | Solo declara métodos, sin implementación.           |
| **Herencia**             | Puede heredar de otra clase (herencia simple).| Puede ser implementada por varias clases.           |
| **Instanciación**        | Se puede instanciar un objeto.              | No se puede instanciar.                             |
| **Atributos**            | Puede tener atributos (variables de instancia).| No puede tener atributos, solo constantes.          |
| **Constructores**        | Puede tener constructores.                  | No tiene constructores.                             |

---

### C. ¿Cuál es la diferencia entre un método estático y uno no estático?

La diferencia entre un **método estático** y un **método no estático** radica en cómo se accede a ellos, su relación con los objetos de una clase, y qué tipo de datos pueden manipular.

#### Diferencias clave:

| **Característica**        | **Método estático**                               | **Método no estático**                           |
|---------------------------|---------------------------------------------------|--------------------------------------------------|
| **Pertenencia**            | Pertenece a la **clase**.                         | Pertenece a una **instancia** de la clase.       |
| **Acceso**                 | Se llama usando el nombre de la clase.           | Se llama usando un objeto instanciado.           |
| **Acceso a atributos**     | Solo puede acceder a miembros estáticos.         | Puede acceder a todos los atributos y métodos.   |
| **Necesidad de instanciación** | No requiere crear un objeto.                   | Requiere crear un objeto.                        |
| **Contexto del estado**    | No tiene acceso al estado del objeto (`this`).   | Puede acceder y manipular el estado del objeto (`this`). |

---

### D. ¿Qué es un ciclo de Vida de Software?

El **Ciclo de Vida de Software (SDLC)** es un conjunto de fases que describen cómo se desarrolla, implementa, mantiene y retira un sistema de software, con el objetivo de cumplir los requisitos del cliente, en tiempo y calidad.

**Fases principales**:
1. **Análisis de requisitos**: Definir las necesidades del cliente y documentar requisitos funcionales y no funcionales.
2. **Diseño**: Crear la arquitectura y estructura del software, incluyendo diseño de alto nivel (HLD) y bajo nivel (LLD).
3. **Implementación**: Desarrollo del software según el diseño, usando lenguajes y herramientas adecuados.
4. **Pruebas**: Evaluar el software con pruebas unitarias, de integración, sistema y aceptación.
5. **Implementación**: Desplegar el software en producción para los usuarios finales.
6. **Mantenimiento**: Corregir errores, añadir mejoras y adaptar el software a nuevos entornos.
7. **Retiro**: Retirar el software cuando ya no sea útil o sea reemplazado.

**Modelos comunes**:
- **Cascada**: Secuencial, ideal para proyectos con requisitos claros.
- **Iterativo**: Desarrolla el software en ciclos con retroalimentación.
- **Ágil**: Entregas incrementales y flexibilidad ante cambios.
- **Espiral**: Combina iteración con análisis de riesgos.
- **DevOps**: Flujo continuo entre desarrollo, pruebas y operaciones.

---

### E. ¿Cuál es la diferencia entre `throw;` y `throw ex;` dentro de un `catch`?

- **throw;**: Relanza la misma excepción sin modificarla, conservando la información de la pila de llamadas.
- **throw ex;**: Crea y lanza una nueva excepción a partir de la capturada, lo que puede perder detalles de la excepción original.


## 2. Algoritmos: 
Son los archivos creados con Python

## 3. Análisis de Modelado de datos:

![Modelo entidad relación](image.png)

Para mayor facilidad las consultas SQL estan en el archivo Postaman enviado a traves del correo, estas consultas son originarias de PostgresSQL
# Cuestionario

- Cuenta de Ahorro con mayor número de titulares
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/get_max_count' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg'
```

- Deuda total de Tarjeta de Crédito por Franquicia
```bash
curl --location --request GET 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/obtener_deuda_total_por_franquicia' \
--header 'Content-Type: application/json' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
```

- Cliente con mayor Saldo en Canje
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/obtener_cliente_mayor_saldo' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
```

- Cliente con mayor saldo retirado de una Cuenta de Ahorros en un periodo determinado. (Por fecha  de transacción)
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/obtener_cliente_mayor_saldo_retirado' \
--header 'Content-Type: application/json' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
--data '{
    "fecha_inicio": "2024-01-01",
    "fecha_fin": "2024-12-31"
}'
```

- Saldo Total de todas las cuentas de ahorro de un cliente.
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/obtener_saldo_total_con_nombre' \
--header 'Content-Type: application/json' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
--data '{"id_cliente": 31}'
```

- Numero de Cuentas de Ahorro activas de clientes extranjeros.
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/contar_cuentas_extranjeros_activas' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
```
- Cuentas de Ahorro activas de clientes extranjeros con nombre
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/obtener_cuentas_extranjeros_activas' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
```
- Listado de Accionistas que son clientes con su correspondiente Saldo Total de Deuda de todas las  tarjetas de crédito cuyo Saldo Total de Deuda sea mayor a UN MILLÓN DE PESOS.
```bash
curl --location 'https://avjbkelvdrstzhtycerf.supabase.co/rest/v1/rpc/obtener_saldo_deuda_accionistas' \
--header 'apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2amJrZWx2ZHJzdHpodHljZXJmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1NzM1NTIsImV4cCI6MjA1MzE0OTU1Mn0.NzHEhMijn9RYmRpntd6bXkWUEdOsNBDS-KNMGMUBgBg' \
```
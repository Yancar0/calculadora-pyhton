# Pruebas del proyecto "Calculadora en Python"

## 1. Descripción general
Este documento describe las pruebas realizadas sobre el proyecto **Calculadora en Python**, el cual implementa operaciones básicas (suma, resta, multiplicación y división).  
Las pruebas se ejecutan con el framework estándar `unittest`.

---

## 2. Tipos de pruebas

### 2.1 Prueba unitaria – `test_suma`
**Objetivo:** Verificar que la función `suma(a, b)` devuelva el resultado correcto.  
**Entrada:** `a = 3`, `b = 5`  
**Resultado esperado:** `8`  
**Resultado obtenido:** `8`  
**Estado:** Aprobada

---

### 2.2 Prueba unitaria – `test_resta`
**Objetivo:** Verificar que la función `resta(a, b)` devuelva el resultado correcto.  
**Entrada:** `a = 5`, `b = 2`  
**Resultado esperado:** `3`  
**Resultado obtenido:** `3`  
**Estado:** Aprobada

---

### 2.3 Prueba de integración – `test_operaciones_encadenadas`
**Objetivo:** Probar la interacción entre las funciones `suma()` y `multiplicacion()`.  
**Ejemplo:** `(3 + 5) * 2 = 16`  
**Resultado esperado:** `16`  
**Resultado obtenido:** `16`  
**Estado:** Aprobada

---

### 2.4 Prueba de rendimiento – `test_rendimiento`
**Objetivo:** Evaluar la eficiencia al repetir una operación muchas veces.  
**Procedimiento:** Ejecutar un millón de sumas consecutivas (`suma(1, 2)`).  
**Resultado esperado:** La prueba debe completarse sin errores en un tiempo razonable (< 1 segundo en equipos modernos).  
**Estado:** Aprobada

---

### 2.5 Prueba adicional – `test_division_por_cero`
**Objetivo:** Confirmar que el programa maneja adecuadamente divisiones entre cero.  
**Resultado esperado:** Lanza `ValueError`.  
**Estado:** Aprobada

---

## 3. Conclusiones
Las pruebas unitarias e integradas aseguran la correcta funcionalidad de las operaciones básicas.  
La prueba de rendimiento confirma que el sistema puede manejar un gran número de operaciones sin fallar.

---

**Autores:** *Equipo de desarrollo: Juan Carlos Sánchez Galicia, Maria Guadalupe Carbajal, Sandra Paola Limon Flores, Karla Rosas Pérez*  
**Fecha:** Octubre 2025  
**Lenguaje:** Python 3.12.3

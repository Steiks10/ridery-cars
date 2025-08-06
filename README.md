# Ridery Cars - Odoo 16

Este repositorio contiene dos módulos principales para Odoo 16:

## ridery_vehicle

Este módulo extiende y complementa el módulo estándar de **Fleet** de Odoo, proporcionando una gestión completa de vehículos y conductores. Permite administrar información detallada de los vehículos, asignación de conductores, servicios relacionados y configuraciones adicionales. Además, incluye una integración con una aplicación web externa para sincronizar y gestionar datos en tiempo real, facilitando la operación y el control de la flota desde cualquier lugar.

### Características principales:
- Gestión avanzada de vehículos y conductores.
- Integración con el módulo Fleet de Odoo.
- Configuración y personalización de servicios de flota.
- Sincronización con una aplicación web externa.

## ridery_log

Este módulo se encarga de registrar los logs de respuesta provenientes de integraciones con terceros. Permite agrupar los registros, establecer reglas de permisos y gestionar el acceso a la información de los logs, asegurando trazabilidad y control sobre las interacciones externas.

### Características principales:
- Registro detallado de logs de integración con terceros.
- Gestión de grupos y reglas de permisos para acceso a los logs.
- Facilita la auditoría y el monitoreo de las integraciones.

---

Ambos módulos están diseñados para mejorar la gestión de flotas y la trazabilidad de integraciones en Odoo 16, proporcionando herramientas robustas y flexibles para empresas que requieren control y automatización en sus operaciones.

## Instalación

1. Copia las carpetas `ridery_vehicle` y `ridery_log` en el directorio `addons` de tu instancia de Odoo 16.
2. Reinicia el servidor de Odoo.
3. Ingresa a Odoo como administrador.
4. Ve al menú **Apps** y actualiza la lista de aplicaciones.
5. Busca e instala los módulos `Ridery Vehicle` y `Ridery Log`.
6. Configura los permisos y parámetros según tus necesidades.

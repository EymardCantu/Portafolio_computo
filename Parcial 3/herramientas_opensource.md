# Herramientas Opensource para Cómputo de Alto Desempeño

Opensource se refiere a código abierto, lo cual permite a cualquiera examinar el código fuente del software. Dentro de estos permisos, es posible mejorar o corregir errores existentes. Esto contrasta con el software de código cerrado. Las principales diferencias son:

**Fiabilidad:** Una gran comunidad de desarrolladores revisa, prueba y corrige constantemente el código opensource, lo que tiende a hacerlo más seguro y estable con menos errores. En cambio, el código cerrado puede tener más errores debido a actualizaciones menos frecuentes y un menor número de desarrolladores involucrados.

**Seguridad:** En el opensource, las vulnerabilidades pueden ser descubiertas y resueltas rápidamente por la comunidad. Los problemas de seguridad se pueden reportar y solucionar en poco tiempo. El código cerrado corre el riesgo de exponer a los usuarios por períodos más largos debido a ciclos de actualización más lentos.

**Licencias:** El opensource ofrece la libertad de acceder y modificar el código fuente para proyectos personales o modificarlo manteniendo la apertura de los cambios. El código cerrado, bajo licencias propietarias, restringe la visualización, modificación o redistribución del código sin permiso.

## Tipos de Herramientas Comúnmente Usadas para Código Abierto en Cómputo:

* **Sistemas operativos:** El software base que controla el hardware de la computadora.
    * **Linux:** Un SO de código abierto que impulsó la computación de alto rendimiento, permitiendo clústeres más accesibles y optimizaciones para tareas científicas.

* **Programadores:** Software que administra y distribuye las tareas de computación en un clúster.
    * **SLURM:** Un programador de tareas de código abierto muy utilizado en grandes clústeres HPC.
    * **Abierto a pedido (Open OnDemand):** Una interfaz web sencilla para interactuar con SLURM.
    * **Motor de cuadrícula (Grid Engine):** Un programador con una historia de código abierto y cerrado, actualmente con una versión comercial activa.
    * **OpenPBS:** Un programador de código abierto originalmente desarrollado para la NASA.
    * **HTCondor:** Un programador que utiliza recursos inactivos de estaciones de trabajo.
    * **Kubernetes:** Un programador de contenedores con creciente interés en HPC.

* **Bibliotecas para computación paralela:** Herramientas que permiten que las aplicaciones utilicen múltiples procesadores simultáneamente.
    * **OpenMP:** Para paralelismo dentro de un mismo nodo (computadora).
    * **OpenMPI:** Para comunicación y trabajo conjunto entre diferentes nodos.
    * **MPICH:** Otra implementación popular de MPI.
    * **MVAPICH:** Una implementación de MPI de alto rendimiento.

* **Proveedores de clúster:** Herramientas para configurar y gestionar grandes grupos de servidores.
    * **MAAS (Metal as a Service):** Para el aprovisionamiento automatizado de hardware.
    * **xCAT (Extreme Cloud Administration Toolkit):** Para gestionar clústeres Linux, especialmente sin disco.
    * **Warewulf:** Un sistema operativo ligero para aprovisionar clústeres.

* **Almacenamiento:** Sistemas para guardar y acceder a grandes cantidades de datos.
    * **Ceph:** Almacenamiento escalable y tolerante a fallos, con opciones de archivos.
    * **Lustre:** Un sistema de archivos paralelo de alto rendimiento.
    * **BeeGFS:** Otro sistema de archivos paralelo para HPC.
    * **DAOS (Distributed Asynchronous Object Storage):** Almacenamiento rápido que utiliza tecnologías modernas.

* **Cargas de trabajo:** Las aplicaciones y tareas específicas que se ejecutan en sistemas HPC.
    * **BLAST (Basic Local Alignment Search Tool):** Para comparar secuencias biológicas.
    * **OpenFOAM (Open Field Operation and Manipulation):** Para simular fluidos.
    * **ParaView:** Para visualizar y analizar datos científicos.
    * **WRF (Weather Research and Forecasting Model):** Para predecir el clima.
    * **Simulador de dinámica de incendios (FDS) y SmokeView (SMV):** Para simular incendios y humo.

* **Contenedores:** Tecnología para empaquetar aplicaciones con todo lo que necesitan para ejecutarse fácilmente.
    * **LXD:** Administrador de contenedores y máquinas virtuales Linux.
    * **Docker:** Plataforma popular para contenedores de aplicaciones.
    * **Singularity/Apptainer:** Contenedores seguros para entornos multiusuario en HPC.
    * **Charliecloud:** Contenedores sin privilegios basados en imágenes Docker.

## Referencias

¿Qué es el código abierto? - Explicación del código abierto - AWS. (n.d.). Amazon Web Services, Inc. [https://aws.amazon.com/es/what-is/open-source/](https://aws.amazon.com/es/what-is/open-source/)

Metal as a Service | MAAS. (2022, November 28). MAAS. https://maas.io/blog/open-source-in-hpc-part-5
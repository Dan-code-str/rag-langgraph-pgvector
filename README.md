# PGVector con LangGraph RAG

Un proceso modular de «generación aumentada por recuperación» que utiliza LangChain, LangGraph y una base de datos PGVector en Docker.

## ⚙️ Instalación y ejecución
1. Iniciar la base de datos: `docker-compose up -d`
2. Instalar las dependencias: `pip install -r requirements.txt`
3. Añadir la API KEY al archivo `.env`.
4. Ejecutar: `python main.py`

---

## 📊 Sample Inputs and Outputs

Para demostrar el funcionamiento de este sistema RAG, se probó el proceso con dos conjuntos de datos completamente diferentes, con el fin de demostrar que recupera el contexto con precisión independientemente del ámbito.

### Caso de prueba 1: [Universidad Nacional de Colombia]

#### Fase de ingestión
* **Input Data (`sample_data.txt`):** 
  > "La Universidad Nacional de Colombia (UNAL) es una universidad pública colombiana de ámbito nacional, fundada bajo el gobierno de Santos Acosta el 22 de septiembre de 1867. Está vinculada a la historia y producción académica de América Latina. Su campus insignia, la Ciudad Universitaria de Bogotá, es el más grande del país y cuenta con 17 edificios declarados monumento nacional. Tiene sedes en Medellín, Manizales, Palmira, Arauca, Leticia, Tumaco, San Andrés y La Paz (Cesar).Su población estudiantil es de 57 106 estudiantes, de los cuales 49 789 son de pregrado y 7317 de posgrado; lo que la convierte en una de las academias colombianas con mayor número de estudiantes. Cuenta también con un total de 2939 docentes activos de planta, la mitad con doctorado. Posee 97 programas de pregrado, 86 especializaciones, 40 especialidades médicas y odontológicas, 171 maestrías y 70 doctorados distribuidos en sus 9 sedes.El 9 de abril de 2010, el Ministerio de Educación Nacional le otorgó la Acreditación Institucional de Alta Calidad por 10 años en todas sus sedes. Numerosas clasificaciones la han ubicado como la mejor del país. Es miembro de la Asociación Colombiana de Universidades, la Asociación Universitaria Iberoamericana de Postgrado (AUIP) y la Red Iberoamericana de Universidades "Universia"."
* **Output:**
  ```text
  Ingestión
  Documento separado en 4 chunks.
  Completado

#### Fase de consulta

* **Input usuario: "¿Quién es el rector de la unal?"**

* **Output:**
  ```text
    === RESPUESTA ===
    Pregunta: ¿Quién es el rector de la unal?
    Respuesta: No puedo responder a esto basándome en los documentos proporcionados.
    ====================

* **Input usuario: "¿Quién es el rector de la unal?"**

* **Output:**
  ```text
    === RESPUESTA ===
    Pregunta: ¿Cuántas maestrías ofrece la unal?
    Respuesta: 171 maestrías.
    ====================

* **Input usuario: "¿Cuántos estudiantes activos y profesores tiene?"**

* **Output:**
  ```text
    === RESPUESTA ===
    Pregunta: ¿Cuántos estudiantes activos y profesores tiene?
    Respuesta: La Universidad Nacional de Colombia tiene una población estudiantil de 57,106 estudiantes, de los cuales 49,789 son de pregrado y 7,317 de posgrado. Además, cuenta con un total de 2,939 docentes activos de planta, la mitad de ellos con doctorado.
    ====================

### Caso de prueba 2: [Colombia]

#### Fase de ingestión
* **Input Data (`sample_data.txt`):** 
  > "Colombia, oficialmente República de Colombia, es un país soberano situado en la región noroccidental de América del Sur. Se constituye en un Estado unitario, social y democrático de derecho, cuya forma de gobierno es de república presidencialista; con dos cámaras legislativas (Cámara de Representantes y Senado), cuyos miembros son elegidos por sufragio directo, voluntario y secreto, con cuatro años de mandato. Su capital y ciudad más poblada es Bogotá. Es una república organizada políticamente en treinta y dos departamentos descentralizados y el Distrito Capital de Bogotá, sede del Gobierno Nacional.Incluyendo la isla de Malpelo, el cayo Roncador y el banco Serrana, el país abarca una superficie terrestre de 1 141 748 km² y un dominio marítimo de 928 660 km², por lo que es el vigesimoquinto país más grande del mundo y el séptimo más grande de América. Reclama como mar territorial el área hasta las 12 millas náuticas de distancia, manteniendo un diferendo limítrofe al respecto con Venezuela y Nicaragua. Limita al norte, con el océano Atlántico; al este, con Venezuela y Brasil; al sur con Perú y Ecuador; y al oeste, con el océano Pacífico y Panamá. Tiene costas en el océano Pacífico y acceso al Atlántico a través del mar Caribe, donde posee diversas islas como el archipiélago de San Andrés, Providencia y Santa Catalina. Es el vigesimoséptimo país más poblado del mundo, con una población de 53 millones de habitantes, además es la segunda nación con más hispanohablantes, detrás de México. Posee una población multicultural, la cual refleja la influencia de la colonización europea a gran escala, pueblos nativos y mano de obra africana, con oleadas migratorias provenientes de Europa y Oriente Medio durante los siglos XIX y XX. El producto interno bruto de paridad de poder adquisitivo de Colombia ocupa el cuarto puesto en América Latina y el puesto 28 a nivel mundial. El PIB nominal colombiano es el cuarto más grande de América Latina y ocupa el puesto 28 a nivel mundial. La presencia humana en Colombia se remonta a más de 14 500 años. Después de miles de años de formación cultural, en el actual territorio colombiano surgieron diversas culturas precolombinas como los muiscas, taironas y quimbayas. Al colonizar a estas culturas, España creó el virreinato de Nueva Granada con capital en Santafé (hoy Bogotá). Tras el inicio de la independencia en 1810 y un periodo marcado por la inestabilidad y guerras civiles durante los siglos XIX y XX, el país ha enfrentado un prolongado conflicto armado interno desde 1960. En 2012 se iniciaron diálogos de paz con las FARC-EP, resultando en un acuerdo final en 2016 que fue implementado con modificaciones en 2017 tras no ser aprobado en un plebiscito. Actualmente, el Gobierno avanza en la implementación de dichos acuerdos y busca nuevas conversaciones con el ELN."

* **Output:**
  ```text
  Ingestión
  Documento separado en 8 chunks.
  Completado

#### Fase de consulta

* **Input usuario: "¿Qué puesto ocupa Colombia en población a nivel mundial y cuántos habitantes tiene?"**

* **Output:**
  ```text
    === RESPUESTA ===
    Pregunta: ¿Qué puesto ocupa Colombia en población a nivel mundial y cuántos habitantes tiene?
    Respuesta: Colombia ocupa el vigesimoséptimo puesto en población a nivel mundial, con una población de 53 millones de habitantes.
    ====================

* **Input usuario: "¿Qué culturas precolombinas existieron?"**

* **Output:**
  ```text
    === RESPUESTA ===
    Pregunta: ¿Qué culturas precolombinas existieron?
    Respuesta: Los muiscas, taironas y quimbayas.
    ====================

* **Input usuario: "¿Quién es el actual presidente de Colombia?"**

* **Output:**
  ```text
    === RESPUESTA ===
    Pregunta: ¿Quién es el actual presidente de Colombia?
    Respuesta: No puedo responder a esto basándome en los documentos proporcionados.
    ====================
# Guide del vault — Referencia original

## Contenido

- Reglas de inicio y continuidad.
- Ejemplo de entrevista.
- PRD V1, modelo de dominio y PRD V2.
- Sitemap, Route Specs y diseño.
- Stacks frontend, backend y DevOps.
- Panel Kanban.

---

- Antes de comenzar con esta guía debemos comprobar primero si existe una carpeta con el nombre del proyecto, por ende debemos de pedir el nombre del proyecto, si el nombre dado no existe dentro de la carpeta "proyectos" que se encuentra en la raíz de este vault, debemos de crear una carpeta con ese nombre, esto es bloqueante, si no se hace no podemos seguir.
- Después de eso debemos de verificar la entrevista, este es un documento que se encuentra dentro de la carpeta del proyecto, se llama "Entrevista", si es que tiene información, seguimos con el siguiente paso. si no tiene entrevista, no podremos seguir hasta que se cree el archivo con información.
- Si ya tenemos la carpeta con el proyecto y el documento "Entrevista" con información, debemos de consultarle al usuario si quiere ir a un paso en especifico (Debemos de listarle los pasos de mas abajo que están enumerados a excepción del "1 - Entrevista con el cliente" ) o darle la opción de ir al siguiente paso de donde quedo, los documentos en orden son, PRD V1, Modelo de dominio ERD, PRD V2, Sitemap, Route Specs, Design Constraints, Stack Frontend, Stack Backend, Stack DevOps, Panel Kanban.

# 1 - Entrevista con el cliente
### Ejemplo
La entrevista se situara al rededor de 5 bloques que comprondran la entrevista

- Cuéntame a qué se dedica hoy tu negocio, cómo funciona y cuál es el servicio principal que entregas.

    - Actualmente el negocio está enfocado en atención nutricional personalizada para pacientes que buscan mejorar su alimentación, bajar de peso, ganar masa muscular o tratar alguna condición específica. La atención se hace principalmente de forma online, aunque también puede haber controles presenciales. El servicio principal consiste en una evaluación inicial, controles periódicos, seguimiento del progreso del paciente y entrega de pautas o minutas personalizadas.

        Hoy gran parte del trabajo depende de la nutricionista directamente. Ella atiende, registra información, revisa exámenes, arma recomendaciones y responde dudas de seguimiento. No hay una plataforma central, por lo que la operación depende mucho del orden manual de cada profesional.

- ¿Quiénes participan en el proceso y qué hace cada uno?

    - Los usuarios principales son la nutricionista y el paciente.

        La **nutricionista** es quien administra casi todo el proceso: registra al paciente, revisa antecedentes, carga controles, compara evolución, entrega observaciones y define recomendaciones o minutas. También necesita consultar rápidamente el historial para no perder tiempo entre sesiones.

        El **paciente** necesita ver su información, revisar indicaciones, consultar avances y posiblemente acceder a documentos o material que la profesional le comparta.

        En una etapa futura podría existir un rol de **asistente administrativa**, que ayude con agendamiento, carga inicial de datos o tareas operativas, pero ese rol no es prioritario para la primera versión.

- ¿Cómo hacen hoy el trabajo desde que entra un cliente hasta que termina el servicio o seguimiento?

    - Actualmente el proceso comienza cuando el paciente agenda o contacta por WhatsApp o Instagram. Luego se recopilan algunos datos básicos de forma manual. La información del paciente puede quedar repartida entre formularios, mensajes, notas, PDFs y archivos sueltos.

        Cuando se hace la primera consulta, la nutricionista registra antecedentes, medidas, objetivos y observaciones en documentos o herramientas separadas. En los controles posteriores revisa esa información anterior manualmente, compara cambios y vuelve a registrar nuevos datos.

        Los exámenes, fotos, archivos o pautas también suelen quedar guardados en carpetas o chats, por lo que buscarlos después consume tiempo. El seguimiento entre controles muchas veces se resuelve por WhatsApp, lo que hace difícil mantener un historial claro y ordenado.

- ¿Qué cosas hoy les hacen perder tiempo, generar errores o trabajar de forma incómoda?

    - Uno de los principales dolores es la **dispersión de la información**. Los datos del paciente no están centralizados, por lo que revisar historial o retomar un caso antiguo toma más tiempo del necesario.

        Otra fricción importante es que el trabajo administrativo consume demasiado tiempo. Registrar controles, revisar documentos previos, comparar evolución y preparar recomendaciones implica pasar por varias herramientas o archivos.

        También hay dificultad para mantener un seguimiento claro del paciente. Parte de la comunicación queda en chats y parte en documentos, así que no siempre es fácil ver el contexto completo de una persona en un solo lugar.

        Además, al no existir una estructura fija, puede haber diferencias en cómo se registra la información entre un paciente y otro, lo que vuelve más difícil estandarizar la atención y escalar el servicio.

- Si pudieras mejorar esto con tecnología, ¿qué te gustaría lograr o tener?

    - La clienta quiere una plataforma donde toda la información del paciente quede centralizada y sea fácil de consultar. Le gustaría poder entrar al perfil de una persona y ver rápidamente antecedentes, controles, evolución, exámenes, documentos y recomendaciones en un solo lugar.

        También quiere reducir el tiempo administrativo que dedica a cada atención, de manera que pueda enfocarse más en analizar al paciente y menos en ordenar archivos o buscar datos. Le interesa que el sistema ayude a mantener una estructura clara para registrar controles y seguimiento.

        A futuro le gustaría que el paciente también pueda entrar a una vista propia para revisar parte de su información, como indicaciones, avances o documentos compartidos. Pero en una primera etapa, su prioridad es mejorar la operación interna y tener un flujo de trabajo más ordenado y escalable.
### Consideraciones
Ten en cuenta que para los proyectos bases, tienes que tener siempre en consideración las rutas de auth (login, register, recovery password) y paginas por default (Mantenimiento y 404) y la pagina de settings para editar la información personal, estas vistas tienen que estar en todos los proyectos con sistema de usuarios.

# 2 - PRD V1
__Prompt__
[[Prompt PRD V1]]
# 3 - Modelo de dominio ERD
__Prompt__
[[Prompt Modelo de dominio ERD]]
- Usa [dbdiagram](https://dbdiagram.io/) para modelar el diagrama de base de datos.
### Ejemplo
```
Table profile {
  id uuid [pk]
  user_id uuid [not null, unique]
  name varchar [not null]
  identifier varchar [not null, unique]
  birthdate varchar [not null]
  phone varchar [not null]
  email varchar [default: null, unique]
  gender varchar [default: null]
  country varchar [default: null]
  isActive boolean [default: true]
  onboarding_complete boolean [default: false]
  identifier_verified boolean [default: false]
}

// Ref: user.id > profile.user_id

Table role {
  id uuid [pk]
  name varchar [not null, unique]
  isActive boolean [default: true]
}

Table profile_role {
  id uuid [pk]
  profile_id uuid [not null]
  role_id uuid [not null]
  assigned_by uuid [default: null]
  assigned_at datetime [not null]
  revoked_by uuid [default: null]

  Indexes {
    (profile_id)
    (role_id)
    (profile_id, role_id) [unique]
  }
}

Ref: profile_role.profile_id > profile.id
Ref: profile_role.role_id > role.id

Table module {
  id uuid [pk]
  name varchar [not null, unique]
  isActive boolean [default: true]
}

Table profile_module {
  id uuid [pk]
  profile_id uuid [not null]
  module_id uuid [not null]
  assigned_by uuid [default: null]
  assigned_at datetime [not null]
  revoked_by uuid [default: null]
  starts_at datetime [default: null]
  ends_at datetime [default: null]
  canceled_at datetime [default: null]
  source varchar [default: null]

  Indexes {
    (profile_id)
    (module_id)
    (profile_id, module_id) [unique]
    (ends_at)
  }
}

Ref: profile_module.profile_id > profile.id
Ref: profile_module.module_id > module.id

Table patient {
  id uuid [pk]
  name varchar [not null]
  identifier varchar [not null, unique]
  birthdate varchar [not null]
  phone varchar [not null]
  email varchar [default: null, unique]
  gender varchar [default: null]
  country varchar [default: null]
  city varchar [default: null]
  job varchar [default: null]
  working_hours varchar [default: null]
  children int [default: 0]
  goal varchar [default: null]
  exist_user boolean [default: false]
  isActive boolean [default: true]
}

Table profile_patient {
  id uuid [pk]
  profile_id uuid [not null]
  patient_id uuid [not null]

  Indexes {
    (profile_id)
    (patient_id)
    (profile_id, patient_id) [unique]
  }
}

Ref: profile_patient.profile_id > profile.id
Ref: profile_patient.patient_id > patient.id

Table nutrition_checkups {
  id uuid [pk]
  patient_id uuid [not null]
  name varchar [default: ""]
  check_date datetime
  isActive boolean [default: true]
  hidden boolean [default: true]
  status varchar [not null, default: "new"]

  Indexes {
    (patient_id)
  }
}

Ref: nutrition_checkups.patient_id > patient.id

Table anthropometric_measurements {
  id uuid [pk]
  nutrition_checkup_id uuid [not null, unique]
  weight decimal [default: 0]
  has_kidney_issues boolean [default: false]
  dry_weight decimal [default: 0]
  height decimal [default: 0]
  wrist_circumference decimal [default: 0]
  waist_circumference decimal [default: 0]
  mid_upper_arm_circumference decimal [default: 0]
  triceps_skinfold decimal [default: 0]
  biceps_skinfold decimal [default: 0]
  calf_circumference decimal [default: 0]
  is_pregnant boolean [default: false]
  gestational_week int [default: 0]
  pre_pregnancy_weight decimal [default: 0]
  gestational_weight decimal [default: 0]
  notes text
}

Ref: anthropometric_measurements.nutrition_checkup_id > nutrition_checkups.id

Table clinical_records {
  id uuid [pk]
  nutrition_checkup_id uuid [not null, unique]
  diseases text
  family_history text
  symptoms_last_month text
  surgical_history text
  daily_medication_use text
}

Ref: clinical_records.nutrition_checkup_id > nutrition_checkups.id

Table habit_logs {
  id uuid [pk]
  nutrition_checkup_id uuid [not null, unique]
  uses_alcohol boolean [default: false]
  alcohol_frequency text
  uses_tobacco boolean [default: false]
  tobacco_frequency text
  uses_drugs boolean [default: false]
  drugs_frequency text
  bedtime text
  effective_sleep_hours int [default: 0]
  lost_sleep_hours int [default: 0]
  does_physical_activity boolean [default: false]
  physical_activity_type text
  physical_activity_frequency text
  physical_activity_duration_estimated text
  physical_activity_level text
  bristol_stool_scale int [default: 0]
  bowel_movements_per_day int [default: 0]
  bowel_movements_per_week int [default: 0]
}

Ref: habit_logs.nutrition_checkup_id > nutrition_checkups.id

Table eating_habits {
  id uuid [pk]
  nutrition_checkup_id uuid [not null, unique]
  food_allergies text
  food_intolerances text
  food_preferences text
  food_aversions text
  swallowing text
  dentition text
  grocery_shopper text
  anxiety text
  anxiety_trigger_foods text
}

Ref: eating_habits.nutrition_checkup_id > nutrition_checkups.id

Table r24h {
  id uuid [pk]
  nutrition_checkup_id uuid [not null]
  meal_time time [not null]
  meal_name varchar [not null]
  foods text

  Indexes {
    (nutrition_checkup_id)
    (nutrition_checkup_id, meal_time)
  }
}

Ref: r24h.nutrition_checkup_id > nutrition_checkups.id

Table food_category {
  id uuid [pk]
  name varchar [not null, unique]
  isActive boolean [default: true]
}

Table food {
  id uuid [pk]
  name varchar [not null]
  calories decimal [default: 0]
  protein decimal [default: 0]
  carbohydrates decimal [default: 0]
  lipids decimal [default: 0]
  serving_unit varchar [default: null]
  serving_size decimal [default: null]
  isActive boolean [default: true]

  Indexes {
    (name)
  }
}

Table food_category_map {
  id uuid [pk]
  food_id uuid [not null]
  food_category_id uuid [not null]

  Indexes {
    (food_id)
    (food_category_id)
    (food_id, food_category_id) [unique]
  }
}

Ref: food_category_map.food_id > food.id
Ref: food_category_map.food_category_id > food_category.id

Table dietary_recall_24 {
  id uuid [pk]
  nutrition_checkup_id uuid [not null]
  food_id uuid [not null]
  servings decimal [not null, default: 0]

  Indexes {
    (nutrition_checkup_id)
    (food_id)
    (nutrition_checkup_id, food_id) [unique]
  }
}

Ref: dietary_recall_24.nutrition_checkup_id > nutrition_checkups.id
Ref: dietary_recall_24.food_id > food.id

Table consumption_trends {
  id uuid [pk]
  nutrition_checkup_id uuid [not null]
  food_id uuid [not null]
  weekly_intake numeric
  notes text

  Indexes {
    (nutrition_checkup_id)
    (food_id)
    (nutrition_checkup_id, food_id) [unique]
  }
}

Ref: consumption_trends.nutrition_checkup_id > nutrition_checkups.id
Ref: consumption_trends.food_id > food.id

Table nutrition_requirements {
  id uuid [pk]
  nutrition_checkup_id uuid [not null, unique]
  factor int
  protein numeric
  carbohydrates numeric
  lipids numeric
}

Ref: nutrition_requirements.nutrition_checkup_id > nutrition_checkups.id

Table meal_plans {
  id uuid [pk]
  patient_id uuid [not null]
  nutrition_checkup_id uuid [default: null]
  name varchar [default: ""]
  calories numeric [default: 0]
  protein numeric [default: 0]
  carbohydrates numeric [default: 0]
  lipids numeric [default: 0]
  show_patient boolean [default: false]
  status varchar [not null, default: "new"]
  isActive boolean [default: true]

  Indexes {
    (patient_id)
    (nutrition_checkup_id)
  }
}

Ref: meal_plans.nutrition_checkup_id > nutrition_checkups.id
Ref: meal_plans.patient_id > patient.id

Table meal_plan_food {
  id uuid [pk]
  meal_plan_id uuid [not null]
  food_id uuid [not null]
  serving_size decimal [default: 0]

  Indexes {
    (meal_plan_id)
    (food_id)
    (meal_plan_id, food_id) [unique]
  }
}

Ref: meal_plan_food.meal_plan_id > meal_plans.id
Ref: meal_plan_food.food_id > food.id

Table meal_slots {
  id uuid [pk]
  name varchar [not null, unique]
  code varchar [not null, unique]
  isActive boolean [default: true]
}

Table meal_plan_food_slot_servings {
  id uuid [pk]
  meal_plan_food_id uuid [not null]
  meal_slot_id uuid [not null]
  serving_size decimal [default: 0]

  Indexes {
    (meal_plan_food_id)
    (meal_slot_id)
    (meal_plan_food_id, meal_slot_id) [unique]
  }
}

Ref: meal_plan_food_slot_servings.meal_plan_food_id > meal_plan_food.id
Ref: meal_plan_food_slot_servings.meal_slot_id > meal_slots.id
```

# 4 - PRD V2
__Prompt__
[[Prompt PRD V2]]
# 5- Sitemap
__Prompt__
[[Prompt Sitemap]]
### Ejemplo
Roles: admin, nutri-base, patient
Modulos: core, admin, nutri-base, patient

| Ruta                                              | Roles               | Modulos             | Objetivo                                                                                                                                                                                                                                            |
| ------------------------------------------------- | ------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/login`                                          |                     |                     | Autenticar a un usuario existente con credenciales o Google.                                                                                                                                                                                        |
| `/register`                                       |                     |                     | Crear una cuenta base para entrar al sistema y continuar a onboarding.                                                                                                                                                                              |
| `/recovery-password`                              |                     |                     | Iniciar recuperación de acceso para usuarios registrados.                                                                                                                                                                                           |
| `/maintenance`                                    |                     |                     | Mostrar indisponibilidad controlada del sistema cuando aplique mantenimiento.                                                                                                                                                                       |
| `/404`                                            |                     |                     | Resolver rutas inexistentes o accesos a vistas no disponibles.                                                                                                                                                                                      |
| `/onboarding`                                     | all                 | core                | Completar datos base del profile y cerrar el estado inicial de ingreso.                                                                                                                                                                             |
| `/settings`                                       | all                 | core                | Editar información personal y ajustes básicos del usuario autenticado.                                                                                                                                                                              |
| `/admin`                                          | admin               | admin               | Dashboard del admin donde podrá visualizar información de la app en general.                                                                                                                                                                        |
| `/admin/users`                                    | admin               | admin               | Listar los usuarios en una tabla con filtros, paginados y accionables de crear y editar.                                                                                                                                                            |
| `/admin/modules`                                  | admin               | admin               | Listar los módulos en una tabla con filtros, paginados y accionables de crear y editar.                                                                                                                                                             |
| `/admin/roles`                                    | admin               | admin               | Listar los roles en una tabla con filtros, paginados y accionables de crear y editar.                                                                                                                                                               |
| `/pro`                                            | nutri-base<br>admin | nutri-base<br>admin | Dashboard de profesional con la información pertinente para el.                                                                                                                                                                                     |
| `/pro/patients`                                   | nutri-base<br>admin | nutri-base<br>admin | Listar, buscar y acceder a pacientes existentes, además de iniciar alta de ficha clínica.                                                                                                                                                           |
| `/pro/patients/:patientId`                        | nutri-base<br>admin | nutri-base<br>admin | Ver información detallada del paciente, poder editar perfil, tener tabs con el listado de los controles y minutas, poder ver los controles, filtrarlos y crear un nuevo control; lo mismo para las minutas.                                         |
| `/pro/patients/:patientId/checkups/:checkupId`    | nutri-base<br>admin | nutri-base<br>admin | Poder ver la información de un control, rellenar cada sección de un control, duplicar un control, descargar el PDF con la información del control o copiar toda la información del control en JSON.                                                 |
| `/pro/patients/:patientId/checkups/compare`       | nutri-base<br>admin | nutri-base<br>admin | Poder buscar controles dentro de un select y seleccionarlos para compararlos según sus atributos cuantificables.                                                                                                                                    |
| `/pro/patients/:patientId/meal-plans/:mealPlanId` | nutri-base<br>admin | nutri-base<br>admin | Poder rellenar una tabla de alimentos y modificar sus porciones para completar la información nutricional requerida por paciente. Después se pueden crear bloques de comida donde se asignan las comidas por porciones a esos bloques alimenticios. |
| `/pro/foods`                                      | nutri-base<br>admin | nutri-base<br>admin | Mantenedor de alimentos con tab de alimento y categoría de alimentos. Cada uno tendrá una tabla con sus filtros.                                                                                                                                    |
| `/pro/meal-slot`                                  | nutri-base<br>admin | nutri-base<br>admin | Mantenedor de bloques de alimentos. Se podrá listar en una tabla, crear registros y editarlos.                                                                                                                                                      |
| `/patient`                                        | patient<br>admin    | patient<br>admin    | Dashboard del paciente donde aparecerán sus controles y minutas. Estarán divididas por módulos: nutricionista, psicólogo, etc. Cada control/minuta tendrá a su profesional.                                                                         |
| `/patient/checkups/:checkupId`                    | patient<br>admin    | patient<br>admin    | Poder ver la información del control, descargarlo en PDF o copiar el prompt en JSON.                                                                                                                                                                |
| `/patient/meal-plans/:mealPlanId`                 | patient<br>admin    | patient<br>admin    | Poder ver la información de la minuta, descargarla en PDF o copiar el prompt en JSON.                                                                                                                                                               |
# 6- Route Specs
__Prompt__
[[Prompt Route Specs]]
# 7 - Design Constraints
Si vas a usar MUI, crea un figma nuevo a base de este [figma](https://www.figma.com/design/3QPmyOJmyBORUFXOeaWpr5/Material-UI-for-Figma--and-MUI-X---Community-?m=auto&t=brydUVVeldREnVb9-6)
Teniendo las rutas, genera la UI con Stitch de google usa el siguiente prompt para el diseño:
__Prompt__
[[Prompt Design Constraints]]
# 8 - Stack Tecnologico
## 8.1 Frontend
__Prompt__
[[Prompt Stack Frontend]]
## 8.2 Backend
__Prompt__
[[Prompt Stack Backend]]
## 8.3 DevOps
__Prompt__
[[Prompt Stack DevOps]]
# 9 - Panel Kanban
__Prompt__
[[Prompt Panel Kanban]]

# Rest API - Gestao de ocorrencias
Rest API Django para gestão de ocorrências em ambiente urbano (Exercício Python & Django)

Requisitos:
 - Python
 - Django
 - djangorestframework
 - django-filter
 
 Como correr o projecto:
  1) $ cd RestProject
  2) $ python manage.py runserver

URLs:
  - Lista de todas as ocorrências: http://127.0.0.1:8000/occurrence/
  - Ocorrência: http://127.0.0.1:8000/occurrence/<id>/, onde id é o id da ocorrência.
  
Especificações:
  Uma ocorrência tem como atributos:
   - description - descrição da mesma;
   - lat - latitude;
   - lon - longitude;
   - owner - autor da ocorrência;
   - initial_date - data e hora da criação da ocorrência;
   - edit_date - data e hora da última edição da ocorrência;
   - state - estado da ocorrência. Opções: [por validar, validado, resolvido];
   - category - categoria da ocorrência. Opções: [CONSTRUCTION, SPECIAL_EVENT, INCIDENT, WEATHER_CONDITION, ROAD_CONDITION].
   
Permissões:
  - Listar ocorrências: todos.
  - Criar ocorrência: apenas utilizadores registados.
  - Editar ocorrência: um administrador pode editar todas as ocorrências, um utilizador normal só pode editar as ocorrências criadas por si.



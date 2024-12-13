from .models import CarMake, CarModel

def initiate():
    print("Iniciando la inserción de datos...")
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instance = CarMake.objects.create(name=data['name'], description=data['description'])
        print(f"Marca creada: {car_make_instance.name}")  # Verifica que se crea cada marca
        car_make_instances.append(car_make_instance)

    car_model_data = [
        {"name":"Pathfinder", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
        {"name":"Qashqai", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
        {"name":"XTRAIL", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[0]},
        {"name":"A-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
        {"name":"C-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
        {"name":"E-Class", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[1]},
        {"name":"A4", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
        {"name":"A5", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
        {"name":"A6", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[2]},
        {"name":"Sorrento", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
        {"name":"Carnival", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[3]},
        {"name":"Cerato", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[3]},
        {"name":"Corolla", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
        {"name":"Camry", "car_type":"Sedan", "year": 2023, "car_make":car_make_instances[4]},
        {"name":"Kluger", "car_type":"SUV", "year": 2023, "car_make":car_make_instances[4]},
    ]
    
    for i, data in enumerate(car_model_data):
        try:
            print(f"Procesando entrada {i}: {data}")
            
            # Verifica que 'name' y 'car_type' estén presentes
            if 'name' not in data or 'car_type' not in data:
                print(f"Error: El elemento en la posición {i} no tiene 'name' o 'car_type'. Datos: {data}")
                continue

            car_type = data.get('car_type')
            if not car_type:
                print(f"Error: No se encontró 'car_type' en los datos de la posición {i}: {data}")
                continue
            if car_type not in dict(CarModel.CAR_TYPE_CHOICES):
                print(f"Error: {car_type} no es un tipo de coche válido.")
                continue

            car_model_instance = CarModel.objects.create(
                name=data['name'],
                car_make=data['car_make'],
                car_type=car_type,
                year=data['year']
            )
            print(f"Modelo creado: {car_model_instance.name} - Marca: {car_model_instance.car_make.name}")
        except KeyError as e:
            print(f"Error de clave: {e} en los datos de la posición {i}: {data}")
        except Exception as e:
            print(f"Error inesperado: {e} en los datos de la posición {i}: {data}")

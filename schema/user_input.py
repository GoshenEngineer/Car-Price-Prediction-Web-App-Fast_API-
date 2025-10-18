from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated


#pydantic model to validate incoming data
class UserInput(BaseModel):
    brand: Annotated[Literal[
         'Maruti', 'Hyundai', 'Ford', 'Renault', 'Mini', 'Mercedes-Benz',
       'Toyota', 'Volkswagen', 'Honda', 'Mahindra', 'Datsun', 'Tata',
       'Kia', 'BMW', 'Audi', 'Land Rover', 'Jaguar', 'MG', 'Isuzu',
       'Porsche', 'Skoda', 'Volvo', 'Lexus', 'Jeep', 'Maserati',
       'Bentley', 'Nissan', 'ISUZU', 'Ferrari', 'Mercedes-AMG',
       'Rolls-Royce', 'Force'],
    Field(..., description= 'brand of the Vehicle')]
    model: Annotated[Literal['Alto', 'Grand', 'i20', 'Ecosport', 'Wagon R', 'i10', 'Venue',
       'Swift', 'Verna', 'Duster', 'Cooper', 'Ciaz', 'C-Class', 'Innova',
       'Baleno', 'Swift Dzire', 'Vento', 'Creta', 'City', 'Bolero',
       'Fortuner', 'KWID', 'Amaze', 'Santro', 'XUV500', 'KUV100', 'Ignis',
       'RediGO', 'Scorpio', 'Marazzo', 'Aspire', 'Figo', 'Vitara',
       'Tiago', 'Polo', 'Seltos', 'Celerio', 'GO', '5', 'CR-V',
       'Endeavour', 'KUV', 'Jazz', '3', 'A4', 'Tigor', 'Ertiga', 'Safari',
       'Thar', 'Hexa', 'Rover', 'Eeco', 'A6', 'E-Class', 'Q7', 'Z4', '6',
       'XF', 'X5', 'Hector', 'Civic', 'D-Max', 'Cayenne', 'X1', 'Rapid',
       'Freestyle', 'Superb', 'Nexon', 'XUV300', 'Dzire VXI', 'S90',
       'WR-V', 'XL6', 'Triber', 'ES', 'Wrangler', 'Camry', 'Elantra',
       'Yaris', 'GL-Class', '7', 'S-Presso', 'Dzire LXI', 'Aura', 'XC',
       'Ghibli', 'Continental', 'CR', 'Kicks', 'S-Class', 'Tucson',
       'Harrier', 'X3', 'Octavia', 'Compass', 'CLS', 'redi-GO', 'Glanza',
       'Macan', 'X4', 'Dzire ZXI', 'XC90', 'F-PACE', 'A8', 'MUX',
       'GTC4Lusso', 'GLS', 'X-Trail', 'XE', 'XC60', 'Panamera', 'Alturas',
       'Altroz', 'NX', 'Carnival', 'C', 'RX', 'Ghost', 'Quattroporte',
       'Gurkha'], 
    Field(..., description= 'model of the Vehicle')]
    vehicle_age: Annotated[int, Field(...,gt = 0, lt = 50, description= 'The Age of the Vehicle')]
    km_driven: Annotated[int, Field(..., gt = 0, lt = 20000, description= 'Km driven by the vehicle')]
    seller_type: Annotated[Literal['Individual', 'Dealer', 'Trustmark Dealer'], Field(..., description = 'Seller Type of the Vehicle')]
    fuel_type: Annotated[Literal['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'], Field(..., description= 'fuel type of  the Vehicle')]
    transmission_type: Annotated[Literal['Manual', 'Automatic'], Field(..., description= 'The transmission of the vehicle')]
    mileage: Annotated[float, Field(..., gt = 0, lt = 120.0, description= 'mileage cover by the Vehicle')]
    engine: Annotated[int, Field(..., description= 'The Engine of the Vehicle')]
    max_power: Annotated[float, Field(..., gt=0, description= 'The max power of the Vehicle')]
    seats: Annotated[int, Field(..., gt = 0, lt = 11, description= 'Number of seats')]


    @field_validator('brand') 
    @classmethod
    def normalize_brand(cls, v:str) -> str:
      v = v.strip().title()
      return v






    
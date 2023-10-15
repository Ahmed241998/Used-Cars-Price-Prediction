import streamlit as st
import pandas as pd
def app() :
    st.title('Descrption')
    st.write('''<a href="https://www.craigslist.org/about/sites">Craigslist</a> is the world's largest collection of used vehicles for sale, 
             yet it's very difficult to collect all of them in the same place. 
            This dataset includes every used vehicle entry within the United States on Craigslist.
''',unsafe_allow_html =True)
    st.markdown('''
<ul>
  <li>
                <h4>Price</h4> <p> The Price of Each Car Listed in The Data. </p>
                </li>
  <li>
                <h4>Year</h4> <p> The Model Year of Each Car Listed in The Data. </p>
                </li>
  <li>
                <h4>Manufacturer</h4> <p> The Manufacturer of Each Car Listed in The Data. Data has The Following Car Manufacturers<ul> 
                <li> GMC </li> 
                <li> Chevrolet </li> 
                <li> Toyota </li> 
                <li> Ford </li> 
                <li> Jeep </li> 
                <li> Nissan </li> 
                <li> Ram </li> 
                <li> Mazda </li> 
                <li> Cadillac </li> 
                <li> Honda </li>
                <li> Dodge </li> 
                <li> Lexus </li> 
                <li> Jaguar </li> 
                <li> volvo </li> 
                <li> Buick </li> 
                <li> Audi </li>
                <li> Infiniti </li>
                <li> Lincoln </li>
                <li> Alfa-Romeo </li>
                <li> Subaru </li>
                <li> Acura </li>
                <li> Mercedes-benz </li>
                <li> BMW </li>
                <li> Mitsubishi </li>
                <li> Volkswagen </li>
                <li> Porsche </li>
                <li> KIA </li>
                <li> Ferrari </li>
                <li> mitsubishi </li>
                <li> volkswagen </li>
                <li> Mini </li>
                <li> Fiat </li>
                <li> Rover </li>
                <li> Tesla </li>
                <li> Saturn </li>
                <li> Mercury </li>
                <li> harley-davidson </li>
                <li> datsun </li>
                <li> aston-martin </li>
                <li> land rover </li></ul>
                </p>
                </li>
  <li><h4>Condition</h1> 
                <p> The Condition of Each Car Listed in The Data. We have the following Conditions with considering that new condition is like new condition and salvage condition is fair condition
                <ul>
                <li>Excellent</li>
                <li>Good</li>
                <li>Like New</li>
                <li>Fair</li>
                </ul>
                </p>
                </li>
  <li><h4>Cylinders</h1>
                <p>The Number of Cylinders of Each Car Listed in The Data. Data has The Following Car Number Of Cylinder
                <ul>
                <li>3 Cylinders </li>
                <li>4 Cylinders </li>
                <li>5 Cylinders </li>
                <li>6 Cylinders </li>
                <li>8 Cylinders </li>
                <li>10 Cylinders </li>
                <li>12 Cylinders </li>
                <li>Other (Not Specified)</li></ul></p>
                </li>
  <li><h4>Fuel</h4>
                <p>The Fuel Type of Each Car Listed in The Data. Data has The Following Car Fuel Type
                <ul>
                <li>Diesel</li>
                <li>Gas</li>
                <li>Electric</li>
                <li>Hybrid</li>
                <li>Other (Not Specified)</li></ul></p>
                </li>
  <li><h4>Odometer</h4>
                <p>The Traveled Distance of Each Car Listed in The Data.The Odometer is a measurement device that shows the total distance traveled by the car.</p></li>
  <li><h4>Title Status</h4>
                <p>Car Title, also called a pink slip, is a document that is issued by the state that acts as a certificate of legal ownership. When a customer purchases a vehicle, the car title is transferred from the car dealership to the car's new owner. Throughout a car's lifetime, its title will be modified according to its condition.
                 Data has the following Car Titles we will illustrate each of them.
                <ul>
                <li>Clean title: This states that the vehicle has no outstanding financial burden of any kind that would prevent it from being sold.</li>
                <li>Lien title: A lien title is simply the title of a car that has a lien against it.  If a car buyer took out a loan to purchase the vehicle and they haven’t yet completely paid back the loan, they do not own the vehicle outright, and the lien title will note that.</li>
                <li> missing : The Title Status Document is missing</li>
                <li> Parts Only :it’s likely the seller simply doesn’t think it can be repaired, but it’s possible that the car was issued a junk title that cannot legally be driven ever again.
                When a vehicle stops operating normally, or it has been in an accident, drivers will often turn to junkyards and dismantlers to pick up their car and give them a small amount of cash. Then, that junkyard will sell the parts off to other people and make a profit. If the junkyard sells the entire car, it’s usually sold with a junk title, a legal document saying that the car has been rendered as junk and can never be driven on the road again.
                </li>
                <li>Rebuilt title:It is for vehicles that have been significantly rebuilt. It is issued by the insurance company or the place where the rebuilding took place, such as a collision center, body shop, or licensed vehicle rebuilder. The vehicle is legal for use on public roads if it passes a safety inspection. </li>
                <li>Salvage title: This is issued to a car with a major value decrease as a result of a significant accident, subsequent repair, or theft. An automobile is due to receive a salvage title if it loses more than 75% of its original value. having a salvage title reduces a car's value, usually meaning it's no longer eligible for financing. The salvage title is normally issued by the car's insurance company and could even be issued to cars with little or no deterioration. As long as they can pass a safety inspection, cars carrying this title are legal to drive.</li>
                </ul>
                </p>
                </li>
  <li><h4>Transmission</h1>
                <p>The Transmission System Type of Each Car Listed in The Data. Data has The Following Car Number Of Types
                <ul>
                <li>Automatic</li>
                <li>Manual</li>
                <li>Other (Not Specified)</li></ul></p>
                </li>
  <li><h4>Drive</h1>
                <p>The Drive Type of Each Car Listed in The Data. Data has The Following Car Number Of Types
                <ul>
                <li>4WD : Four-Wheel Drive</li>
                <li>RWD : Front-Wheel Drive </li>
                <li>RWD : Rear-Wheel Drive </li></ul></p>
                </li>
    <li><h4>Type</h1>
                <p>The Type of Each Car Listed in The Data. Data has The Following Car Number Of Types
                <ul>
                <li>Bus</li>
                <li>Convertible</li>
                <li>Coupe</li>
                <li>Hatchback</li>
                <li>MiniVan</li>
                <li>Offroad</li>
                <li>Pick Up</li>
                <li>Sedan</li>
                <li>SUV</li>
                <li>Track</li>
                <li>Van</li>
                <li>Wagon</li>
                <li>Other (Not Specified)</li>
                </ul></p>
                </li>
</ul> ''', unsafe_allow_html=True

    )
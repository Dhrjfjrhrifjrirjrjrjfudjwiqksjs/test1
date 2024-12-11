let x = 5
let y ="23"
//Eine Zeilen Kommentar
/* Bis geschlossen */
console.log(y * x)


Operatoren Mathe: +, -, *, /, %, Math.floo(), Math.pow()
Logische Operatoren: ==, !=, <, >, >=, <=, ===, !==


  Listen

let x =[2,3,"Hello"]
console.log(x[0]) = 2 // so kann man einen Wert aussuchen der ausgegeben werden soll allerdings mit Angabe des Index 
x.push(3) = [2,3,"Hello",3] // fügt einen wert ans ende der Liste
x.pop() = "Hello",x = [2,3]
x.shift() = 2,x = [3,"Hello"] // nimmt einen Wert aus der Liste heraus man muss jedoch den Index angeben
x.slice(1,3) = [3,"Hello"] // mit slice kann man auch sachen ersetzen
x.includes(2) = true

let n = [1,2,3,4]
console.log(n.length)
n.splice(3,0"Hallo")
console.log(n)


Objects

let obj = {name:"Jan",age:27,address:{city:"MG"}}
console.log(obj.name);/console.log(obj["name"])
obj.name = "Karl"
obj.address.city
Object.keys(obj)
Object.values(obj)

if_Bedingung

//Grundstruktur
if (Bedingung){
  //Code ausführen, wenn Bedingung wahr ist
} else if (andereBedingung){
  //Code ausführen, wenn andereBedingung wahr ist
} else { 
  //Code ausführen, wenn keine der Bedingung wahr ist
}

Wann welche Schleife verwenden

- for: Wenn du eine bekannte Anzahl von Iterationen hast.
- while: Wenn du eine Bedingung hast, die erfüllt sein muss, aber die Iterationsanzahl unklar ist.
- do...while: Wenn du sicherstellen musst, dass der Code mindestens einmal ausgeführt wird.
- for...of: Wenn du über Elemente eines Arrays oder Strings interierst
- for...in: Wenn du die Eigenschaften eines Objekts durchlaufen wills. 


for (Initialisierung;Bedingung;Iteration){
  //Code, der wiederholt ausgeführt wird 
}
Beispiel
for (let i = 0;i < 5; i++){
  console.log("Interation",i);
}

while (Bedingung){
  //Code, der wiederholt ausgeführt wird 
}
Beispiel
let i = 0;
while (i < 5){
  console.log("Iteration",i);
  i++;
}

do{
  //Code, der mindestens einmal ausgeführt wird 
} while (Bedingung);
Beispiel 
let i = 0;
do{
  console.log("Iteration";i);
  i++;
}while (i < 5);

for (let element of iterable){
  //Code, der für jedes Element ausgeführt wird 
}
Beispiel
let obst = ["Apfel","Banane","Kirsche"]
for (let frucht of obst){
  console.log(frucht);
}

for (let key in object){
  //Code, der für jede Eigenschaft ausgeführt wird
}
Beispiel
let person = {name: "Max",alter:25,Stadt:"Berlin"};
for(let eigenschaft in person){
  console.log(eigenschaft, ":", person[eigenschaft]);
  }
Hello world
let x = 5
let y ="23"
//Eine Zeilen Kommentar
/* Bis geschlossen */
console.log(y * x)


Operatoren Mathe: +, -, *, /, %, Math.floo(), Math.pow()
Logische Operatoren: ==, !=, <, >, >=, <=, ===, !==


  Listen

let x =[2,3,"Hello"]
console.log(x[0]) = 2 // so kann man einen Wert aussuchen der ausgegeben werden soll allerdings mit Angabe des Index 
x.push(3) = [2,3,"Hello",3] // fügt einen wert ans ende der Liste
x.pop() = "Hello",x = [2,3]
x.shift() = 2,x = [3,"Hello"] // nimmt einen Wert aus der Liste heraus man muss jedoch den Index angeben
x.slice(1,3) = [3,"Hello"] // mit slice kann man auch sachen ersetzen
x.includes(2) = true

let n = [1,2,3,4]
console.log(n.length)
n.splice(3,0"Hallo")
console.log(n)


Objects

let obj = {name:"Jan",age:27,address:{city:"MG"}}
console.log(obj.name);/console.log(obj["name"])
obj.name = "Karl"
obj.address.city
Object.keys(obj)
Object.values(obj)

if_Bedingung

//Grundstruktur
if (Bedingung){
  //Code ausführen, wenn Bedingung wahr ist
} else if (andereBedingung){
  //Code ausführen, wenn andereBedingung wahr ist
} else { 
  //Code ausführen, wenn keine der Bedingung wahr ist
}

Wann welche Schleife verwenden

- for: Wenn du eine bekannte Anzahl von Iterationen hast.
- while: Wenn du eine Bedingung hast, die erfüllt sein muss, aber die Iterationsanzahl unklar ist.
- do...while: Wenn du sicherstellen musst, dass der Code mindestens einmal ausgeführt wird.
- for...of: Wenn du über Elemente eines Arrays oder Strings interierst
- for...in: Wenn du die Eigenschaften eines Objekts durchlaufen wills. 


for (Initialisierung;Bedingung;Iteration){
  //Code, der wiederholt ausgeführt wird 
}
Beispiel
for (let i = 0;i < 5; i++){
  console.log("Interation",i);
}

while (Bedingung){
  //Code, der wiederholt ausgeführt wird 
}
Beispiel
let i = 0;
while (i < 5){
  console.log("Iteration",i);
  i++;
}

do{
  //Code, der mindestens einmal ausgeführt wird 
} while (Bedingung);
Beispiel 
let i = 0;
do{
  console.log("Iteration";i);
  i++;
}while (i < 5);

for (let element of iterable){
  //Code, der für jedes Element ausgeführt wird 
}
Beispiel
let obst = ["Apfel","Banane","Kirsche"]
for (let frucht of obst){
  console.log(frucht);
}

for (let key in object){
  //Code, der für jede Eigenschaft ausgeführt wird
}
Beispiel
let person = {name: "Max",alter:25,Stadt:"Berlin"};
for(let eigenschaft in person){
  console.log(eigenschaft, ":", person[eigenschaft]);
  }









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










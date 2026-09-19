//Fazer uma tabuada de matematica
for (let numero = 1; numero <= 10; numero++) {
  console.log(`Tabuada do ${numero}`);

  for (let multiplicador = 1; multiplicador <= 10; multiplicador++) {
    console.log(`${numero} x ${multiplicador} = ${numero * multiplicador}`);
  }

  console.log('');
}

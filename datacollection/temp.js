fs.readFile('./CityList.txt', function (err, data) {
  if (err) throw err;
  console.log(data);
});

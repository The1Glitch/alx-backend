import { CreateClient, print } from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.log(`Redis client not connect to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
   client.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(err), result) {
     if (error) {
       console.log(error);
       throw error;
     }
     console.log(result);
  }):
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSabFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

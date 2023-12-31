/**
 * Get all databases
 */

 const { CloudantV1 } = require("@ibm-cloud/cloudant");
 const { IamAuthenticator } = require("ibm-cloud-sdk-core");
 
 function main(params) {
   const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY });
   const cloudant = CloudantV1.newInstance({
     authenticator: authenticator,
   });
   cloudant.setServiceUrl(params.COUCH_URL);
 
   let dbList = getDbs(cloudant);
   return { dbs: dbList };
 }
 
 function getDbs(cloudant) {
   cloudant
     .getAllDbs()
     .then((body) => {
       body.forEach((db) => {
         dbList.push(db);
       });
     })
     .catch((err) => {
       console.log(err);
     });
 }

main({
  "COUCH_URL": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
  "IAM_API_KEY": "lQK4AYTSTQoZeA--BQtSMGiXn8n8HRNlcAKR-UWO9Sl8",
  "COUCH_USERNAME": "premsai0809@gmail.com"
})
function myFunction() {

  var data = {

  text: "hello"

};

var payload = JSON.stringify(data);

var options = {

  method: "POST",

  contentType: "application/json; charset=UTF-8",

  payload: payload,

  muteHttpExceptions: true

};

  var webhook = 'https://chat.googleapis.com/v1/spaces/-uCgP4AAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=6eL1z-DExif5d8fYzkbNE8ORWpIiIq_1aEjufZEakT0%3D';

  var response = UrlFetchApp.fetch(webhook, options);

  Logger.log(response.getContentText());

}

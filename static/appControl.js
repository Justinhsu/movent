'use strict';

  var app = angular.module('movent-app', ['ngRoute']);
  var serverName = 'http://localhost:5000';//this needs to change based on where we host the code
  app.config(function($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider.
      when('/', {
        templateUrl: '/static/page.html',
        controller: 'pageController'
      });
  });


  app.controller('pageController', function($http, $scope, $interval, $timeout) {
    $scope.data = {
      eventTitle: "",
      color: "",
      repeat: "",
      busy: "",
      startDateTime:"",
      endDateTime:""
    };


    $scope.generate = function() {
        $http.post('/generateChart', $scope.data).then(function(data) {
          console.log($scope.data);
        });
    };
  });




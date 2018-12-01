(function() {
  'use strict';

  angular.module('app').config(routerConfig);

  /** @ngInject */
  function routerConfig($stateProvider, $urlRouterProvider) {
    $stateProvider.state('home', {
      url: '/',
      component: 'home',
    });
    $stateProvider.state('todo', {
          url: '/api/task/:id',
          component: 'todoComponent',
          resolve:{
            todoList:function(todoService,$stateParams){
            return todoService.getTasks($stateParams.id);
            }
          }
        });

    $urlRouterProvider.otherwise('/');
  }
})();

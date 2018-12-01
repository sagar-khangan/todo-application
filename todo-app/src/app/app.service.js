(function() {
  'use strict';

  angular.module('app').factory('todoService',ToDoService);

  function ToDoService(API,$http) {
         var service = {};

          service.getTasks = function(id) {
              return $http.get(API+'/todo/'+id)
              .then(function successCallback(response){
                return response.data
            });
          };

          service.addTask = function(task,tasklist){
            var body = {name:task}
            return $http.post(API+'/todo/'+tasklist,body)
          };

          service.updateTask = function(task,tasklist){
            var body = {name:task.name,task_finished:task.task_finished}
            return $http.put(API+'/todo/'+tasklist+'/'+task.id,body)
          };

          service.deleteTask = function(taskid,tasklist){
            return $http.delete(API+'/todo/'+tasklist+'/'+taskid)
          };
          return service;
      }

})();

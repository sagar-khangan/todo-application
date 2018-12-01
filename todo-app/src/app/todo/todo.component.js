(function() {
  'use strict';

  angular.module('app').component('todoComponent', {
    controller: ToDoController,
    controllerAs: 'vm',
    templateUrl: 'app/todo/todo.view.html',
      bindings: {
          todoList: "=",
    }
  });

  function ToDoController($log, $rootScope,$scope,$state, $translate,$stateParams,todoService) {

     var vm = this;
     this.$onInit = function() {
     if (vm.todoList.status == 'Fail'){
        vm.success = false;
        vm.todolist = []
        }
    else{
        vm.success = true;
       vm.todolist = vm.todoList.data;
       }
     };

      vm.update = function(task){
        todoService.updateTask(task,$stateParams.id)
             .then(function successCallback(response){
                $log.debug(response);
               vm.todolist  = todoService.getTasks($stateParams.id).data;
               $state.reload();
            });
        };

       vm.delete = function(taskid){
         todoService.deleteTask(taskid,$stateParams.id)
             .then(function successCallback(response){
             $log.debug(response);
               vm.todolist  = todoService.getTasks($stateParams.id).data;
               $state.reload();
            });
        };

        vm.create = function(task){
            todoService.addTask(task,$stateParams.id)
             .then(function successCallback(response){
             $log.debug(response);
               vm.todolist  = todoService.getTasks($stateParams.id).data;
               $state.reload();
            });
        };

    }
})();

angular.module('BlankApp', ['ngMaterial'])
.controller('myCtrl', function ($scope, $http) {
    $scope.hello = {name: "Boaz"};
    $scope.newName = "";
    $scope.sendPost = function() {
        var data = {
                name: $scope.newName
            };
        $http.post("/soemthing", data).success(function(data, status) {
            $scope.hello = data;
        })
    }
})
.controller('moreCtrl', function($scope) {

});

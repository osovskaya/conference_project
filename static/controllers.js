var ChatControllers = angular.module('ChatControllers', []);

ChatControllers.controller('MyUserCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.user = {};
    $scope.messages = [];
    $scope.channel = 'chat';

    $dragon.onReady(function() {
        $dragon.subscribe('message', $scope.channel, {sender: 1}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });

        $dragon.getSingle('myuser', {id:1}).then(function(response) {
            $scope.user = response.data;
        });

        $dragon.getList('message', {user_id:1}).then(function(response) {
            $scope.messages = response.data;
        });
    });

    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper.mapData($scope.messages, message);
            });
        }
    });
}]);

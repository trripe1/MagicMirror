Module.register("MMM-HandGestures", {
    start: function () {
        this.sendSocketNotification("CONNECT_WS");
    },

    socketNotificationReceived: function (notification, payload) {
        if (notification === "GESTURE_DETECTED") {
            if (payload.gesture === "RIGHT") {
                this.sendNotification("PAGE_NEXT");
            } else if (payload.gesture === "LEFT") {
                this.sendNotification("PAGE_PREVIOUS");
            }
        }
    }
});

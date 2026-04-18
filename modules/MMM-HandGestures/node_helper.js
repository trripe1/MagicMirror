const NodeHelper = require("node_helper");
const WebSocket = require("ws");

module.exports = NodeHelper.create({
    start: function () {
        console.log("MMM-HandGestures helper started...");
    },

    socketNotificationReceived: function (notification, payload) {
        if (notification === "CONNECT_WS") {
            this.connectWS();
        }
    },

    connectWS: function () {
        const ws = new WebSocket("ws://localhost:8080"); // Coincide con Python

        ws.on("message", (data) => {
            try {
                const msg = JSON.parse(data);
                this.sendSocketNotification("GESTURE_DETECTED", msg);
            } catch (e) {}
        });

        ws.on("open", () => console.log("WebSocket conectado desde MMM-HandGestures"));
    }
});

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>A Little Question ❤️</title>

    <style>
        * {
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            margin: 0;
            min-height: 100vh;
            min-height: 100dvh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;

            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Roboto, Helvetica, Arial, sans-serif;

            background:
                radial-gradient(circle at 20% 20%, #ffd6e7 0%, transparent 30%),
                radial-gradient(circle at 80% 80%, #ffc1dc 0%, transparent 30%),
                linear-gradient(135deg, #ffedf5, #fff5fa);

            color: #5a1735;
        }

        .container {
            width: 92%;
            max-width: 500px;
            text-align: center;
            padding: 35px 20px;
            position: relative;
            z-index: 5;
        }

        .heart {
            font-size: 90px;
            animation: heartbeat 1.2s infinite;
            filter: drop-shadow(0 8px 15px rgba(255, 70, 130, 0.3));
            margin-bottom: 10px;
        }

        @keyframes heartbeat {
            0%, 100% {
                transform: scale(1);
            }
            15% {
                transform: scale(1.15);
            }
            30% {
                transform: scale(1);
            }
            45% {
                transform: scale(1.12);
            }
        }

        h1 {
            font-size: clamp(2rem, 9vw, 3.2rem);
            margin: 10px 0;
            line-height: 1.1;
            color: #c9185b;
        }

        .question {
            font-size: clamp(1.2rem, 5vw, 1.6rem);
            line-height: 1.5;
            margin: 20px auto 30px;
            font-weight: 600;
        }

        .buttons {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 18px;
            min-height: 90px;
            position: relative;
        }

        button {
            border: none;
            border-radius: 999px;
            padding: 17px 32px;
            font-size: 1.25rem;
            font-weight: 800;
            cursor: pointer;
            touch-action: manipulation;
            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease,
                background 0.25s ease;
        }

        #yes {
            background: linear-gradient(135deg, #ff3f81, #ff1765);
            color: white;
            box-shadow: 0 8px 20px rgba(255, 23, 101, 0.35);
            z-index: 10;
        }

        #yes:active {
            transform: scale(0.95);
        }

        #no {
            background: white;
            color: #d94b78;
            border: 2px solid #ffb3cb;
            box-shadow: 0 5px 15px rgba(200, 50, 100, 0.12);
            position: relative;
        }

        .tiny-message {
            margin-top: 20px;
            font-size: 0.95rem;
            color: #a54b6e;
            min-height: 25px;
            font-weight: 600;
        }

        /* Celebration */

        #celebration {

            display: none;
            animation: appear 0.8s ease forwards;
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: scale(0.6);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        .yay {
            font-size: clamp(3rem, 14vw, 5.5rem);
            font-weight: 1000;
            color: #ff1765;
            text-shadow: 0 5px 20px rgba(255, 23, 101, 0.25);
            animation: bounce 0.8s infinite alternate;
        }

        @keyframes bounce {
            from {
                transform: rotate(-3deg) scale(1);
            }
            to {
                transform: rotate(3deg) scale(1.08);
            }
        }

        .love-message {
            font-size: 1.4rem;
            line-height: 1.6;
            font-weight: 600;
            margin-top: 20px;
        }

        .floating-heart {
            position: fixed;
            bottom: -50px;
            font-size: 30px;
            pointer-events: none;
            animation: floatUp linear forwards;
            z-index: 100;
        }

        @keyframes floatUp {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 1;
            }

            100% {
                transform: translateY(-120vh) rotate(360deg);
                opacity: 0;
            }
        }

        .sparkle {
            position: fixed;
            pointer-events: none;
            z-index: 90;
            animation: sparkle 1.5s ease-out forwards;
        }

        @keyframes sparkle {
            0% {
                transform: scale(0);
                opacity: 1;
            }

            100% {
                transform: scale(1.5) translateY(-100px);
                opacity: 0;
            }
        }

        /* Make it especially comfortable on small phones */
        @media (max-width: 380px) {
            .heart {
                font-size: 70px;
            }

            button {
                padding: 15px 25px;
                font-size: 1.1rem;
            }

            .question {
                font-size: 1.15rem;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <div id="questionScreen">

        <div class="heart">❤️</div>

        <h1>I Love You!</h1>

        <div class="question">
            I Love you, Will you Marry me Daphne? 💍🥰
        </div>

        <div class="buttons">
            <button id="yes">YES ❤️</button>
            <button id="no">NO 💔</button>
        </div>

        <div class="tiny-message" id="message">
            Choose wisely... 😇
        </div>

    </div>


    <div id="celebration">

        <div class="heart">💖</div>

        <div class="yay">
            YIPPEEEEEEEE!!!
        </div>

        <div class="love-message">
            I knew you'd say yes! 🥰❤️
            <br><br>
            I love you more than anything in the world Wifey :3 ❤.
            <br>
            Forever and always. 💕
        </div>

        <div style="font-size: 45px; margin-top: 25px;">
            💕 💗 💖 💘 💝 💞
        </div>

    </div>

</div>


<script>

    const yesButton = document.getElementById("yes");
    const noButton = document.getElementById("no");
    const message = document.getElementById("message");

    let yesScale = 1;

    const funnyMessages = [
        "Hmmmm... try again 😇",
        "Are you sure? 🥺",
        "That button seems broken... 👀",
        "Nice try! 😂❤️",
        "Keep trying...",
        "The universe says YES. 🌎❤️",
        "You can't escape my love! 💕",
        "Try the other button 😘"
    ];

    let messageIndex = 0;


    /*
        Make YES bigger every time she clicks it.
        It doesn't finish the game until she taps it
        enough times to make it ridiculously cute.
    */
    yesButton.addEventListener("click", function() {

        yesScale += 0.18;

        yesButton.style.transform =
            `scale(${yesScale})`;

        messageIndex++;

        if (messageIndex < funnyMessages.length) {
            message.textContent = funnyMessages[messageIndex];
        }

        // Extra hearts whenever YES is clicked
        createHeartBurst(8);

        // Once she clicks YES enough times, celebrate!
        if (yesScale >= 2.3) {
            setTimeout(showCelebration, 350);
        }
    });


    /*
        The NO button doesn't actually work.
        On phones, it jumps to a random safe position.
    */
    noButton.addEventListener("click", function() {

        message.textContent =
            "NOPE! That button doesn't work 😂❤️";

        moveNoButton();

        // Make YES a little bigger too
        yesScale += 0.12;

        yesButton.style.transform =
            `scale(${yesScale})`;

        createHeartBurst(5);
    });


    /*
        Also make the NO button run away when she gets
        close to it.
    */
    noButton.addEventListener("touchstart", function() {
        moveNoButton();
    });


    function moveNoButton() {

        const padding = 20;

        const maxX =
            window.innerWidth - noButton.offsetWidth - padding;

        const maxY =
            window.innerHeight - noButton.offsetHeight - padding;

        const x =
            Math.max(padding, Math.random() * maxX);

        const y =
            Math.max(padding, Math.random() * maxY);

        noButton.style.position = "fixed";
        noButton.style.left = x + "px";
        noButton.style.top = y + "px";

        noButton.style.transform =
            `rotate(${Math.random() * 20 - 10}deg)`;
    }


    function createHeart() {

        const heart = document.createElement("div");

        heart.className = "floating-heart";

        const hearts = [
            "❤️",
            "💕",
            "💗",
            "💖",
            "💘",
            "💝",
            "💞",
            "🥰"
        ];

        heart.textContent =
            hearts[Math.floor(Math.random() * hearts.length)];

        heart.style.left =
            Math.random() * 100 + "vw";

        heart.style.fontSize =
            (20 + Math.random() * 35) + "px";

        heart.style.animationDuration =
            (3 + Math.random() * 4) + "s";

        document.body.appendChild(heart);

        setTimeout(() => {
            heart.remove();
        }, 7000);
    }


    function createHeartBurst(amount) {

        for (let i = 0; i < amount; i++) {
            setTimeout(createHeart, i * 100);
        }
    }


    function showCelebration() {

        document.getElementById("questionScreen").style.display =
            "none";

        document.getElementById("celebration").style.display =
            "block";

        // MASSIVE heart explosion ❤️
        for (let i = 0; i < 60; i++) {
            setTimeout(createHeart, i * 60);
        }

        message.textContent = "";

        // Keep hearts floating in the background
        setInterval(() => {
            createHeart();
        }, 400);
    }


    // A few hearts are always floating in the background
    setInterval(() => {
        if (document.getElementById("questionScreen").style.display !== "none") {
            createHeart();
        }
    }, 1200);

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

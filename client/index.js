import * as Phaser from "phaser";
import Config from "./src/data/config";
import Game from "./src/scenes/game";

const gameConfig = {
  name: Config.TITLE,
  type: Phaser.AUTO,
  width: Config.WIDTH,
  height: Config.HEIGHT,
  scene: [Game],
};

window.game = new Phaser.Game(gameConfig);

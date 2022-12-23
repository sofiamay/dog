import Phaser from "phaser";
import { addGamePieces } from "../graphics/board-graphics";

export default class Game extends Phaser.Scene {
  constructor() {
    super({
      key: "Game",
    });
  }

  preload() {
  }

  create() {
    let self = this;

    var gamePieces = addGamePieces(this);
  }

  update() {}
}

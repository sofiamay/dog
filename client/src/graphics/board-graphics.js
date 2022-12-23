import Config from "../data/config";
import GameGrid from "../data/grid";

const WHITE_GRID = [
	[9,0], [10,0],[11,0],[12,0],
	[8,1],[12,1]
	// keep going
];

export function addGamePieces(scene) {
	// x,y coordinates are center of circle
	var purpleCircleTest= scene.add.circle(100, 100, 80, 0x6666ff);
	return purpleCircleTest;
}

export default {
  addGamePieces,
};
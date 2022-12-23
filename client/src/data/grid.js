import { WIDTH, HEIGHT, UNIT_SIZE} from "./config";

// Locate spot in grid from top to bottom, left to right
class Grid {
	constructor(width, height, unitSize) {
		this.width = width;
		this.height = height;
		this.unitSize = unitSize;
	}

	// Return [int, int] where each int is an offset in pixels
	locate(x, y) {
		let centerPosition = this.unitSize / 2;
		let xOffset = (unitSize * x) + centerPosition;
		let yOffset = (unitSize * y) + centerPosition;
		if (xOffset > this.width || yOffset > this.height) {
			throw `Grid.locate(${x},${y}): Either x or y is off the grid`;
		}
		return [xOffset, yOffset];
	}

	// ( [[x0,y0], [x1,y1, [int, int], [...]] ) => [[x0Px, y0Px],[x1Px, y1Px],[int, int], [...]]
	locateAll(arr) {
		let result = [];
		arr.forEach((coordinate) => {
			let x = coordinate[0];
			let y = coordinate[1]
			let offset = this.locate(x, y);
			result.push(offset);
		});
		return result;
	}


}

const GameGrid= new Grid();
export default GameGrid;
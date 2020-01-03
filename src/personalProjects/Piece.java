package personalProjects;

/**
 * The class for determining the state of the board pieces
 *
 * @Author Richard Erickson and Melanie Andromidas
 * @Version 0.0.1
 */
public class Piece {
    private boolean isCaptured;
    private boolean hasEscaped;
    private Type type;

    /**
     * Constructor, takes the Type enum to set the type of piece
     *
     * @param piece
     */
    public Piece(Type piece) {
        isCaptured = false;
        hasEscaped = false;
        type = piece;
    }

    /**
     * Method to set the piece to have been captured
     */
    public void justCaptured() {
        isCaptured = true;
    }

    /**
     * Method to detect if the piece has been captured
     */
    public boolean hasBeenCaptured() {
        return isCaptured;
    }

    /**
     * Method to set the piece to have run away
     */
    public void runAway() {
        hasEscaped = true;
    }

    /**
     * Method to see if a piece has escaped
     */
    public boolean gottenAway() {
        return hasEscaped;
    }

    /**
     * Method to determine the type of piece
     */
    public Type typeOfPiece() {
        return type;
    }
}

layout(matrix(c(1,2,3,4), 2,2, byrow=FALSE))
par(xpd=FALSE)
par(oma=c(0,2,0,0))
colfill = c("purple", "darkgreen", "blue", "orange")
plot(movementmeans$one, type="l", col="purple", main="Changes in card positions", 
     xlab="Round", ylab="Average changes in card positions")
lines(movementmeans$two, type="l", col="darkgreen")
lines(movementmeans$three, type="l", col="blue")
lines(movementmeans$six, type="l", col="orange")
abline(v=time.stable[1,], col=colfill, lty=2)


plot(movementsds$one, type="l", col="purple", main="Variability of changes in card positions",
     xlab="Round", ylab="Standard deviation of changes in card positions",
     ylim=c(0,14), yaxt="n")
axis(2, at=seq(0,14, by=2))
abline(v=time.stable[1,], col=colfill, lty=2)
lines(movementsds$two, type="l", col="darkgreen")
lines(movementsds$three, type="l", col="blue")
lines(movementsds$six, type="l", col="orange")

plot(1, type="n", axes=FALSE, xlab="", ylab="")
par(xpd=NA)
legend("top", title="Deck number", c("one","two","three","six"), fill=colfill,
       cex=.7, horiz=TRUE, bty="n")
mtext("Vertical lines indicate average round at \nwhich the decks reach stability",
     side=1)

boxplot(time.stable~deck.number, data=data, main="Number of rounds to reach stability",
        ylab="Number of Decks", xlab="Number of Rounds", col=colfill, notch=TRUE,
        horizontal=TRUE)
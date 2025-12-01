const fs = require('fs');

function main() {
    // console.log("Hello World!");

    fs.readFile('./sample.txt', 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            return;
        }

        console.log(data);
    })
}

if (require.main === module) {
    main();
}
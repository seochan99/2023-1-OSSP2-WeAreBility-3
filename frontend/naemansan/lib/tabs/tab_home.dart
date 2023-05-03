//홈 페이지 Home()
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 2,
        foregroundColor: Colors.black87,
        backgroundColor: Colors.white,
        title: Row(
          children: [
            Padding(
              padding: const EdgeInsets.only(left: 20.0),
              child: Row(
                children: const [
                  Text(
                    '내만산',
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  SizedBox(width: 8),
                  Icon(
                    Icons.forest_outlined,
                    color: Colors.green,
                  ),
                ],
              ),
            ),
            const Spacer(),
            const Icon(
              Icons.notifications_none_sharp,
              color: Colors.black,
            ),
            const SizedBox(width: 20),
          ],
        ),
      ),
    );
  }
}

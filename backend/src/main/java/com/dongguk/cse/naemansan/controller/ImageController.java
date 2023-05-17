package com.dongguk.cse.naemansan.controller;

import com.dongguk.cse.naemansan.common.ExceptionDto;
import com.dongguk.cse.naemansan.domain.type.ImageUseType;
import com.dongguk.cse.naemansan.common.ResponseDto;
import com.dongguk.cse.naemansan.service.ImageService;
import com.sun.nio.sctp.IllegalUnbindException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/image")
public class ImageController {
    private final ImageService imageService;

    @PostMapping("/user")
    public ResponseDto<?> uploadImage(Authentication authentication, @RequestParam("image")MultipartFile file) throws IOException {
        log.info("이미지 저장 요청 | User: {}", Long.valueOf(authentication.getName()));
        Map<String, String> map = new HashMap<>();
        map.put("uuidname", imageService.uploadImage(Long.valueOf(authentication.getName()), ImageUseType.USER, file));
        return new ResponseDto(map);
    }

    @GetMapping("/{fileName}")
    public ResponseEntity<?> downloadImage(@PathVariable String fileName) throws IOException {
        byte[] imageData = imageService.downloadImage(fileName);

        // 임시 체크
        if (imageData.length == 0)
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(ResponseDto.builder()
                            .success(false)
                            .data(null)
                            .error(new ExceptionDto(new IllegalUnbindException())).build());
        else
            return ResponseEntity.status(HttpStatus.OK)
                .contentType(MediaType.valueOf("image/png"))
                .body(imageData);
    }
}
